from django.db import models

# Create your models here.

class Player(models.Model):
    JERSEY_SIZES= [
    ('S','SMALL'),
    ('M', 'MEDIUM'),
    ('L', 'LARGE')
    ]
    position_options = models.TextChoices("position_options", "MIDFIELD DEFENDER STRIKER GOALKEEPER")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    shirt_size = models.CharField(max_length=5,choices=JERSEY_SIZES)
    position= models.CharField(max_length=10, choices=position_options.choices, null=True)

class Match(models.Model):
    match_date=models.DateField()
    match_type=models.CharField(max_length=10)
    players=models.ManyToManyField(Player, through='TeamSelection')

class TeamSelection(models.Model):
    player=models.ForeignKey(Player, on_delete=models.CASCADE)
    match= models.ForeignKey(Match, on_delete=models.CASCADE)
    starting=models.BooleanField()