import uuid
from django.db import models
from django.contrib.auth.models import User
from sports.models import Sport

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='events')
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100, default="IET Agra Sports Club")
    registration_deadline = models.DateTimeField()
    description = models.TextField()
    poster = models.ImageField(upload_to='events/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    registration_id = models.CharField(max_length=20, unique=True, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    category_position = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def save(self, *args, **kwargs):
        if not self.registration_id:
            self.registration_id = f"IET-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.registration_id} - {self.student_name}"