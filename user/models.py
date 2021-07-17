from django.db import models
from advisor.models import Advisor
from datetime import datetime

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=20)


class Booking(models.Model):
    advisor_id = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.CharField(max_length=299)
