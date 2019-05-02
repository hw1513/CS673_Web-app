from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Programs
from .forms import ProgramForm
from django.contrib import messages
from todo_list.models import List


def detail(request, program_name):
    """
    This function gets and renders all project members within the program and renders them in the detail template

    :param request:
    :param program_name:
    :return:
    """
    program = get_object_or_404(Programs, project_name=program_name)
    members = list(program.project_members.all())
    return render(request, 'programs/detail.html', {'program': program, 'members': members})


def program(request):
	"""
	This function gets all programs and renders them into the programs template

	:param request:
	:return:
	"""

    all_programs = list(Programs.objects.all())

    return render(request, 'programs/programs.html', {'all_programs': all_programs})



def todo_home(request):

	if request.method == 'POST':

		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=List.objects.all()
			messages.success(request, ('Item has been added to list!'))
			return render(request, 'todo_home.html', {'all_items' : all_items , 'form' : form})

	else:



def add_member(request, program_name):
	"""
	This function adds a member to the program with a POST API call and on success renders the additional member
	into the program

	:param request:
	:param program_name:
	:return:
	"""
    program = get_object_or_404(Programs, project_name=program_name)
    if request.method == 'POST':

        form = ProgramForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Program.objects.all()
            messages.success(request, ('New program has been created'))
            return render(request, 'programs/add_member.html', {'all_items': all_items, 'form': form})

    else:

        all_items = Programs.objects.all
        form = ProgramForm()

        return render(request, 'programs/add_member.html', {'all_items': all_items, 'form': form})



def addprogram(request):
	"""
	This function adds a new program using the form with a POST request API call. If the call fails the user is prompted
	again and the template is rendered.

	:param request:
	:return:
	"""

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


