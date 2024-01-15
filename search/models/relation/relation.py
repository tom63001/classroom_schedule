from django.db import models


class Relation_Manager(models.Manager):
    def in_weekday_order(self, *args, **kwargs):
        ORDER = {"M": 0, "T": 1, "W": 2, "R": 3, "F": 4}
        rslt = self.get_queryset().filter(*args, **kwargs)
        return sorted(rslt, key=lambda val: (ORDER[val.weekdays], val.time[6], val.time[0], val.time[1]))


class Relation(models.Model):
    course = models.ForeignKey("search.Course", on_delete=models.CASCADE)
    classroom = models.ForeignKey("search.Room", on_delete=models.CASCADE)
    weekdays = models.CharField(max_length=16)
    time = models.CharField(max_length=16)
    objects = Relation_Manager()

    def serialize(self):
        return {
            "day": self.weekdays,
            "time": self.time,
            "scheduled course": self.course,
            "scheduled classroom": self.classroom
        }
