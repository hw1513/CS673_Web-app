from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Programs
from .forms import ProgramForm

def detail(request, program_name):
	program = get_object_or_404(Programs, project_name=program_name)
	members = list(program.project_members.all())
	return render(request, 'programs/detail.html', {'program':program, 'members':members})

def program(request):
	return render(request, 'programs/programs.html',{})


def add_member(request, program_name):
	program = get_object_or_404(Programs, project_name=program_name)
	if request.method == 'POST':

		form = ProgramForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=Program.objects.all()
			messages.success(request, ('New program has been cretated'))
			return render(request, 'programs/add_member.html', {'all_items' : all_items , 'form' : form})

	else:

		all_items = Programs.objects.all
		form = ProgramForm()

		return render(request, 'programs/add_member.html', {'all_items' : all_items , 'form' : form })

