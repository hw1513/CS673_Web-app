from django.shortcuts import render, redirect
from .models import iList
from .forms import ListForm
from django.contrib import messages


# Create your views here.
def issue_home(request):

	if request.method == 'POST':

		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=iList.objects.all()
			messages.success(request, ('Issue has been added to list!'))
			return render(request, 'issue_home.html', {'all_items' : all_items , 'form' : form})

	else:

		all_items = iList.objects.all
		form = ListForm()

		return render(request, 'issue_home.html', {'all_items' : all_items , 'form' : form })


def delete(request, list_id):
	item = iList.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted!'))
	return redirect('issue_home')




def cross_off(request, list_id):
	item = iList.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('issue_home')

def uncross(request, list_id):
	item = iList.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('issue_home')

def edit(request, list_id):
	if request.method == 'POST':
		item=iList.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=request.user)

		if form.is_valid():
			form.save()
			print('Form is valid')
			
			messages.success(request, ('Issue has been edited!'))
		
			return redirect('issue_home')

	else:

		item = iList.objects.get(pk=list_id)

		return render(request, 'edit_issue.html', {'item' : item})





def addnew(request):
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Added New Issue'))
			return redirect('issue_home')
	else:
		form = ListForm(instance=request.user)

	context = {'form': form}
	return render(request, 'new_issue.html', context)

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

