from django.shortcuts import render, redirect,get_object_or_404
from .models import List
from .forms import ListForm,EditIssue
from django.contrib import messages
from .models import Programs

# Create your views here.
def todo_home(request):

	if request.method == 'POST':

		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=List.objects.all()
			messages.success(request, ('Item has been added to list!'))
			return render(request, 'todo_home.html', {'all_items' : all_items , 'form' : form})

	else:

		all_items = List.objects.all
		form = ListForm()

		return render(request, 'todo_home.html', {'all_items' : all_items , 'form' : form })

def detail(request, list_id):
  item=get_object_or_404(List, pk=list_id)
  #form = EditIssue(instance=item)
  return render(request, 'idetail.html', {'item' : item})
    
    

def delete1(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted!'))
	program = get_object_or_404(Programs, project_name=item.belongs)
	members = list(program.project_members.all())
	all_items = List.objects.all
	return render(request, 'programs/detail.html', {'program':program, 'members':members, 'all_items':all_items})



def cross_off1(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	program = get_object_or_404(Programs, project_name=item.belongs)
	members = list(program.project_members.all())
	all_items = List.objects.all
	return render(request, 'programs/detail.html', {'program':program, 'members':members, 'all_items':all_items})


def uncross1(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	program = get_object_or_404(Programs, project_name=item.belongs)
	members = list(program.project_members.all())
	all_items = List.objects.all
	return render(request, 'programs/detail.html', {'program':program, 'members':members, 'all_items':all_items})



def edit(request, list_id):
	if request.method == 'POST':
		item=List(pk=list_id)

		form = EditIssue(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			print('Form is valid')
			
			messages.success(request, ('Item has been edited!'))
		
			program = get_object_or_404(Programs, project_name=item.belongs)
			members = list(program.project_members.all())
			all_items = List.objects.all
			return render(request, 'programs/detail.html', {'program':program, 'members':members, 'all_items':all_items})


	else:
		item=List(pk=list_id)
		form = EditIssue(instance=item)
		return render(request, 'edit.html', {'form':form})




def addnew_item(request):
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Added New Item'))
			all_programs = list(Programs.objects.all())
			return render(request, 'authenticate/home.html', {'all_programs' : all_programs,})

	else:
		form = ListForm(instance=request.user)

	context = {'form': form}
	return render(request, 'new_todo.html', context)

"""
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Profile'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
"""

