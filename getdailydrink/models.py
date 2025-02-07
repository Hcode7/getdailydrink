from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User= get_user_model()

class UserWaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=500)
    water_amount = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

