from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


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


def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted!'))
	return redirect('todo_home')




def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('todo_home')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('todo_home')

def edit(request, list_id):
	if request.method == 'POST':
		item=List.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=request.user)

		if form.is_valid():
			form.save()
			print('Form is valid')
			
			messages.success(request, ('Item has been edited!'))
		
			return redirect('todo_home')

	else:
		print('error')
		item = List.objects.get(pk=list_id)

		return render(request, 'edit.html', {'item' : item})





def addnew(request):
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Added New Item'))
			return redirect('todo_home')
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

