from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Friend
from programs.models import Programs

#def home(request):
	#return render(request, 'authenticate/home.html', {})

def issue(request):
	return render(request, 'authenticate/issue.html',{})

def friend(request):
	Users = User.objects.all()
	friend=Friend.objects.get(current_user=request.user)
	friends=friend.users.all()
	return render(request, 'authenticate/friend.html', {'Users' : Users , 'friends' : friends})

def change_friends(request, operation, pk):
	new_friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, new_friend)
	elif operation == 'remove':
		Friend.lose_friend(request.user, new_friend)
	return redirect('friend')




def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('You Have Been Logged In!'))
			return redirect('home')
		
		else:
			messages.success(request, ('Error logging in - Please Try Again'))
			return redirect('home')

		
	else:
		all_programs = list(Programs.objects.all())
		
		return render(request, 'authenticate/home.html', {'all_programs' : all_programs,})



def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You Have Registered'))
			return redirect('home')
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

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


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Profile'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

