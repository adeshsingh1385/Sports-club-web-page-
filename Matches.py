from django.db import models
from sports.models import Sport, Team, Player

class Match(models.Model):
    STATUS_CHOICES = (
        ('UPCOMING', 'Upcoming'),
        ('LIVE', 'Live'),
        ('COMPLETED', 'Completed'),
    )
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team_b_name = models.CharField(max_length=100, help_text="Opponent Team Name (Internal or External)")
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UPCOMING')
    
    # Live Scores Fields
    score_a = models.CharField(max_length=50, blank=True, default="0")
    score_b = models.CharField(max_length=50, blank=True, default="0")
    overs_commentary = models.CharField(max_length=100, blank=True, help_text="e.g. 14.2 Overs or 2nd Half")
    summary = models.CharField(max_length=255, blank=True, help_text="e.g. IET won by 14 runs")

    def __str__(self):
        return f"{self.team_a.name} vs {self.team_b_name} ({self.sport.name})"

class Leaderboard(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-points', '-wins']

    def __str__(self):
        return f"{self.player.name} - {self.points} Pts"