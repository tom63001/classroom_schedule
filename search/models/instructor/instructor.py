from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=32)
    instructing = models.ManyToManyField("search.Course")

    def __str__(self):
        return self.name
