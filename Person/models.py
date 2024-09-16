from django.db import models

class Person(models.Model):
    cin = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField()
    events = models.ManyToManyField('Event.Event', through='Event.Participation')


    def __str__(self):
        return self.cin
