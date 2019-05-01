from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .models import Programs
from .forms import ProgramForm
from django.contrib import messages

def detail(request, program_name):
	program = get_object_or_404(Programs, project_name=program_name)
	members = list(program.project_members.all())
	return render(request, 'programs/detail.html', {'program':program, 'members':members})

def program(request):
	

		all_programs = list(Programs.objects.all())
		

		return render(request, 'programs/programs.html', {'all_programs' : all_programs })


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

def addprogram(request):
	if request.method == 'POST':
		form = ProgramForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Added New Program'))
			return redirect('programhome')
	else:
		form = ProgramForm(instance=request.user)

	context = {'form': form}
	return render(request, 'programs/addprogram.html', context)
	
def delete_program(request,program_name):
    #program = get_object_or_404(Programs, project_name=program_name)
    one_task=Programs.objects.get(project_name=program_name)
    one_task.delete()
    all_programs = list(Programs.objects.all())
    messages.success(request, ('You Have Deleted Program'))
    return render(request, 'programs/programs.html', {'all_programs' : all_programs })