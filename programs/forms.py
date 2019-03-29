from django import forms
from .models import Programs

class ProgramForm(forms.ModelForm):
	class Meta:
		model = Programs
		fields= ["project_name", "start_date","project_description",]
		