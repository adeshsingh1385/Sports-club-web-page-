from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    sport = models.CharField(max_length=100)
    competition = models.CharField(max_length=200)
    year = models.IntegerField(default=2026)
    position_held = models.CharField(max_length=100, help_text="e.g., Winner, 1st Runner Up")
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return f"{self.title} ({self.year})"

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, default="General")
    is_priority = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('athletics', 'Athletics'),
        ('annual_meet', 'Annual Sports Meet'),
    ])
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"