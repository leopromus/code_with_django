from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
