import datetime
from django.db import models
from django.urls import reverse


class Event(models.Model):
    eventName = models.CharField(max_length=264, unique=True)  # Event Name
    eventDescription = models.TextField()  # About the Event
    eventVenue = models.CharField(max_length=50)  # Venue for the Event
    eventDate = models.DateField(editable=True)  # Event date
    eventStartTime = models.TimeField(editable=True, default=datetime.time(16, 00))  # Event starting time
    eventEndTime = models.TimeField(editable=True, default=datetime.time(18, 00))  # Event ending time
    eventRegEndDate = models.DateField(editable=True)  # Event Registration deadline date
    eventRegEndTime = models.TimeField(editable=True, default=datetime.time(16, 00))  # Event Registration deadline time
    eventSpeaker = models.TextField(editable=True)  # Speakers in the Event
    eventURL = models.URLField(editable=True)  # Event Livestream URL link
    eventDocumentation = models.URLField(editable=True, default='')  # Event Documentation URL link
    eventLogo = models.URLField(
        editable=True,
        default="https://drive.google.com/file/d/1hl6Xt2cnUMC5RUrmXH6w-kQD8fhuF3rC/view?usp=sharing"
    )  # Event image

    def get_absolute_url(self):
        return reverse("eventreg:eventDetails", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.eventName)

    class Meta:
        ordering = ['eventDate']


class EventUserData(models.Model):
    eventName = models.ForeignKey(Event, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=264, unique=True)
    studentReg = models.CharField(max_length=10, unique=True)
    studentEmail = models.EmailField(unique=True)
    studentRegistered = models.BooleanField(default=False)
    studentCheckedIn = models.BooleanField(default=False)
