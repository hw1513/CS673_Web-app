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

		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been edited!'))
			return redirect('todo_home')

	else:

		item = List.objects.get(pk=list_id)

		return render(request, 'edit.html', {'item' : item})
