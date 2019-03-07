from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Programs

def detail(request, program_name):
	program = get_object_or_404(Programs, project_name=program_name)
	return render(request, 'programs/detail.html', {'program':program})

def program(request):
	return render(request, 'programs/programs.html',{})