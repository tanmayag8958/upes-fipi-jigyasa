from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team_count = models.IntegerField(default=1)
    date_registered = models.DateTimeField(default=timezone.now)
    trans_id = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
