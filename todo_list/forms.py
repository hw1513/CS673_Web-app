from django import forms
from .models import List

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields= ["item", "completed", "belongs","assigned","description","start_date"]
		

		
class EditIssue(forms.ModelForm):
	class Meta:
		model = List
		fields = ["item", "completed", "belongs","assigned","description","start_date"]

	def __init__(self, *args, **kwargs):
		super(EditIssue, self).__init__(*args, **kwargs)

