from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    PROGRAMMING = 'PR'
    SPORTS = 'SP'
    HEALTH = 'HE'
    MUSIC = 'MU'
    LIFE = 'LI'
    TRAVEL = 'TR'
    CATEGORY_CHOICES = [
        (PROGRAMMING, 'Programming'),
        (SPORTS, 'Sports'),
        (HEALTH, 'Health'),
        (MUSIC, 'Music'),
        (LIFE, 'Life'),
        (TRAVEL, 'Travel'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=PROGRAMMING,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateField(default=date.today)
    claps = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
