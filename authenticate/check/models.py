from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Check(models.Model):
	"""docstring for check"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	checkIn = models.DateTimeField(auto_now_add=True)
	checkOut = models.DateTimeField(default=timezone.now, null=True)
'''
class Profile(models.Model):
	departments = (
			('IT', 'IT'),
			('RISK', 'RISK'),
			('HR', 'HR'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	department = models.CharField(max_length=1, choices=departments, blank=False)
	email = models.CharField(max_length=50, blank=True)
	checkStatus = models.BooleanField(default=False)
'''