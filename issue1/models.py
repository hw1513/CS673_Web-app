from django.db import models
from programs.models import Programs

class iList(models.Model):
	item = models.CharField(max_length=35)
	completed = models.BooleanField(default=False)
	issuebelongs = models.ForeignKey(Programs, on_delete=models.CASCADE,)

	def __str__(self):
		return self.item + ' | '+ str(self.completed)
