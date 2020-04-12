from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name
