from django.http import JsonResponse
from search.models.rooms.rooms import Room
from search.models.instructor.instructor import Instructor
from django.core.serializers import serialize

import json


def format_json(serialized_json):
    json_data = json.loads(serialized_json)
    json_data = [obj["fields"] for obj in json_data]
    return json_data


def get_suggestions(request):
    if request.method == "GET":
        all_classrooms = Room.objects.all().order_by("name")
        all_instructors = Instructor.objects.all().order_by("name")
        json_classrooms = format_json(serialize("json", all_classrooms))
        json_instructors = format_json(serialize("json", all_instructors))

        return JsonResponse({"all_classrooms": json_classrooms, "all_instructors": json_instructors})
    return JsonResponse({"result": "error"})
