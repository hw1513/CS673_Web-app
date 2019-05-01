from django import forms
from .models import iList

class ListForm(forms.ModelForm):
	class Meta:
		model = iList
		fields= ["item", "completed", "issuebelongs","assigned","start_date"]
		
class EditIssue(forms.ModelForm):
	class Meta:
		model = iList
		fields = ["item", "completed", "issuebelongs","assigned","start_date","description"]

	def __init__(self, *args, **kwargs):
		super(EditIssue, self).__init__(*args, **kwargs)
