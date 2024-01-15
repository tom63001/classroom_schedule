from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=32)
    associated_relation = models.ManyToManyField("search.Course", through="search.Relation")

    def __str__(self):
        return self.name
