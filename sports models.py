from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-running", help_text="FontAwesome icon class")
    image = models.ImageField(upload_to='sports/')
    rules = models.TextField(blank=True)
    coach_name = models.CharField(max_length=100, blank=True)
    training_schedule = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='teams')
    logo = models.ImageField(upload_to='teams/', blank=True, null=True)
    captain_name = models.CharField(max_length=100)
    vice_captain_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.sport.name})"

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='players/', blank=True, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    position = models.CharField(max_length=50)
    jersey_number = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField(default=1)
    achievements = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.sport.name}"