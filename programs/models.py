from django.db import models
from django.contrib.auth.models import User


class Programs(models.Model):

	"""
	This class initializes the class object with the required fields
	"""

    project_name = models.CharField(max_length=20, primary_key=True)
    start_date = models.DateField('date started')
    project_description = models.CharField(max_length=200)
    project_members = models.ManyToManyField(User)


    def __str__(self):
        return self.project_name
