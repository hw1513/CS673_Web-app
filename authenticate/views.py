from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Friend
from programs.models import Programs


# TODO: Charlie can you explain the initial home functionality?

# def home(request):
# 	return render(request, 'authenticate/home.html', {})

def issue(request):
    """
    This function allows you to create issues

    :param request:
    :return:
    """
    return render(request, 'authenticate/issue.html', {})


def friend(request):
    """
    This function is a global helper function
    that allows request to become a friend

    :param request:
    :return:
    """
    users = User.objects.all()

    # TODO: there is a shadow object for friend here that we may need to refactor

    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    return render(request, 'authenticate/friend.html', {'Users': users, 'friends': friends})


def change_friends(request, operation, pk):
    """
    This function implements the ability to add
    and remove friend associations

    :param request:
    :param operation:
    :param pk:
    :return:
    """

    # TODO: What does pk do here? What does it mean?

    new_friend = User.objects.get(pk=pk)

    # This logic implements the adding and removal of friends
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return redirect('friend')


def login_user(request):
    """
    This function makes a POST API call to log into Acadella system.

    :param request:
    :return:
    """

    # If the post request is successful you log in, otherwise this catches the error
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('home')

        else:
            messages.success(request, ('Error logging in - Please Try Again'))
            return redirect('home')

    else:
        return render(request, 'authenticate/home.html', {})


def logout_user(request):
    """
    This function implements the logout functionality

    :param request:
    :return:
    """

    # TODO: I believe we need to implement error handling here

    logout(request)
    messages.success(request, ('You Have Been Logged Out'))
    return redirect('home')


def register_user(request):
    """
    This function implements the register functionality of Acadella platform

    :param request:
    :return:
    """

    # TODO: We need to implement error logging here

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
    """
    This function implements the ability of the user
    to edit the profile via POST API calls.

    :param request:
    :return:
    """

    # This POST API request calls the edit profile form and sends it to
    # form to save the information. Once this completes you get redirected to home
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
    """
    This function allows users to change their passwords via a POST API call

    :param request:
    :return:
    """

    # TODO: Logging required

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

