from django.db import models
from django.contrib.auth.models import User

class Programs(models.Model):
	project_name=models.CharField(max_length=20)
	start_date=models.DateTimeField('date started')
	project_description=models.CharField(max_length=200)
	project_members=models.ManyToManyField(User)
	def __str__(self):
		return self.project_name
