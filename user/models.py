from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	