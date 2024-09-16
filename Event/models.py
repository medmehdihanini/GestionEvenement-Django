from django.db import models

# Create your models here.
from django.db import models
from Person.models import Person

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    category = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    nbr_participant = models.PositiveIntegerField(default=0)
    evt_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField('Person.Person', through='Participation')


    def __str__(self):
        return self.title



class Participation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    participation_date = models.DateField()

    class Meta:
        unique_together = ('person', 'event')  # Empêche une personne de participer plusieurs fois au même événement

    def __str__(self):
        return f'{self.person.cin} participated in {self.event.title} on {self.participation_date}'