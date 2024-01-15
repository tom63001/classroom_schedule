import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from search.models.rooms.rooms import Room
from search.models.course.course import Course
from search.models.instructor.instructor import Instructor
from search.models.relation.relation import Relation


def get_info_web(request):
    print("server: get_info")
    print(request.GET.get("inputValue", None))
    all_classrooms = Room.objects.all().order_by("name")
    all_instructors = Instructor.objects.all().order_by("name")
    if request.method == "GET":
        classroom = Room.objects.filter(name=request.GET.get("inputValue", None))
        if classroom.count() != 0:
            classroom_id = Room.objects.get(name=request.GET.get("inputValue", None)).id
            classroom_info = Relation.objects.in_weekday_order(classroom=classroom_id)
            for info in classroom_info:
                print(info.weekdays, info.time, info.classroom, info.course)

            # serialized = [{"day": info.weekdays, "time": info.time, "scheduled course": info.course.name}
            #              for info in classroom_info]
            return JsonResponse([{"day": info.weekdays, "time": info.time, "scheduled course": info.course.name,
                                  "course title": info.course.title}
                                 for info in classroom_info], safe=False)
        else:
            instructor = Instructor.objects.get(name=request.GET.get("inputValue", None))
            instructing_info = instructor.instructing.all()
            return JsonResponse([{"scheduled course": info.name, "course title": info.title}
                                 for info in instructing_info], safe=False)
    return render(request, "ends/web.html", {"all_classrooms": all_classrooms, "all_instructors": all_instructors})


def get_info(request):
    current_platform = request.GET.get("platform")
    # if current_platform == "Web":
    return get_info_web(request)
