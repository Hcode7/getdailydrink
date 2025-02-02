from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User= get_user_model()

class UserWaterIntake(models.Model):
    # user = models.ForeignKey('users.CustomerUser', on_delete=models.CASCADE)
    water_amount = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)