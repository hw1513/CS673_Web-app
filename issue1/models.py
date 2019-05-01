from django.db import models
from programs.models import Programs
from django.contrib.auth.models import User

class iList(models.Model):
	item = models.CharField(max_length=35)
	description = models.CharField(max_length=400)
	completed = models.BooleanField(default=False)
	issuebelongs = models.ForeignKey(Programs, on_delete=models.CASCADE,)
	assigned = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date=models.DateField('date started')

	def __str__(self):
		return self.item + ' | '+ str(self.completed)
