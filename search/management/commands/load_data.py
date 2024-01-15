import csv

from django.core.management import BaseCommand
from search.models.relation.relation import Relation
from search.models.course.course import Course
from search.models.rooms.rooms import Room
from search.models.instructor.instructor import Instructor


file = open("all_courses_final.csv", "r")
reader = csv.reader(file)
next(reader)


def process(some_str):
    arr = list(some_str)
    while "p" in arr:
        idx = arr.index("p")
        if arr[idx - 6] == "1":
            arr.remove("p")
            pass
        else:
            temp = int(arr[idx - 5])
            if temp + 12 >= 20:
                arr[idx - 6] = "2"
            else:
                arr[idx - 6] = "1"
            temp = (temp + 12) % 10
            arr[idx - 5] = str(temp)
            arr.remove("p")
    while "a" in arr:
        arr.remove("a")
    while "m" in arr:
        arr.remove("m")
    arr.insert(arr.index("-") + 1, ' ')
    rslt = ""
    for c in arr:
        rslt += c
    return rslt


def process2(some_str):
    rslt = some_str.split(" , ")
    return rslt


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Loading classroom data")
        i = 0
        for row in reader:
            print("Writing " + str(i) + "th line into database.")
            i = i + 1
            subject = str(row[0])
            course_code = str(row[1])
            course_title = str(row[3])
            weekdays = str(row[4])
            temp = str(row[5])
            interval = process(temp)
            temp2 = str(row[6])
            instructors = process2(temp2)
            location = str(row[7])
            course_name = subject + ' ' + course_code
            for day in weekdays:
                current_course, course_status = Course.objects.get_or_create(name=course_name, title=course_title)
                current_classroom, classroom_status = Room.objects.get_or_create(name=location)
                current_relation = Relation.objects.create(course=current_course, classroom=current_classroom,
                                                           weekdays=day, time=interval)

            for instructor in instructors:
                current_instructor, instructor_status = Instructor.objects.get_or_create(name=instructor)
                current_course, course_status = Course.objects.get_or_create(name=course_name, title=course_title)
                current_instructor.instructing.add(current_course)

        print("Loading succeeded")
