from django import forms
from .models import iList

class ListForm(forms.ModelForm):
	class Meta:
		model = iList
		fields= ["item", "completed", "issuebelongs"]
		

