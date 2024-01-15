from django.contrib import admin
from search.models.relation.relation import Relation
from search.models.course.course import Course
from search.models.rooms.rooms import Room
from search.models.instructor.instructor import Instructor

# Register your models here.

admin.site.register(Relation)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Instructor)
