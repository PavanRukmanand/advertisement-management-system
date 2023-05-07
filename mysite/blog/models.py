from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin


class Advertiser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cost_per_click = models.DecimalField(max_digits=10, decimal_places=2)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TargetAudience(models.Model):
    age_range = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    interests = models.TextField()

    def __str__(self):
        return f"{self.age_range} {self.gender} {self.location}"

class AdTargeting(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    target_audience = models.ForeignKey(TargetAudience, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ad} -> {self.target_audience}"


