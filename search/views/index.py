import json
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from search.models.rooms.rooms import Room
from search.models.instructor.instructor import Instructor
from django.http import JsonResponse

########################### Pre-React code ######################################################################
# def index(request):
#     print(request.GET)
#     all_classrooms = Room.objects.all().order_by("name")
#     all_instructors = Instructor.objects.all().order_by("name")
#     return render(request, "ends/web.html", {"all_classrooms": all_classrooms, "all_instructors": all_instructors})
#################################################################################################################


@ensure_csrf_cookie
def index(request):
    print("server: index.html")
    return render(request, "ends/index.html")
