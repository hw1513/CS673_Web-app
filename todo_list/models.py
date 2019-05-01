from django.db import models
from programs.models import Programs
from django.contrib.auth.models import User

class List(models.Model):
	item = models.CharField(max_length=35)
	completed = models.BooleanField(default=False)
	belongs = models.ForeignKey(Programs, on_delete=models.CASCADE,)
	description = models.CharField(max_length=400)
	assigned = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date=models.DateField('date started')
	def __str__(self):
		return self.item + ' | '+ str(self.completed)
