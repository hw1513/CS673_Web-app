from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import Http404, HttpResponseForbidden

from django.shortcuts import render

from django.urls import reverse

from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView
from .forms import ComposeForm
from .models import Thread, ChatMessage


class InboxView(LoginRequiredMixin, ListView):
    """
    This class creates an inbox view using the inbox template
    """

    template_name = 'chat/inbox.html'

    def get_queryset(self):
        """
        This is a getter for the thread object

        :return:
        """

        return Thread.objects.by_user(self.request.user)

class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    """
    This class defines the thread view
    """

    template_name = 'chat/thread.html'

    form_class = ComposeForm

    success_url = './'

    #TODO: I believe this method could be inheritied as it's repeated above

    def get_queryset(self):

        return Thread.objects.by_user(self.request.user)



    def get_object(self):
        """
        This method is a getter for the thread between two users to use
        If this fails the web server will 404 Resource not found

        :return:
        """

        other_username  = self.kwargs.get("username")

        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)

        if obj == None:

            raise Http404

        return obj



    def get_context_data(self, **kwargs):
        """
        This method is a recursive function that gets the form details
        and returns the content of the form

        :param kwargs:
        :return:
        """

        # TODO: I don't fully understand this method

        context = super().get_context_data(**kwargs)

        context['form'] = self.get_form()

        return context



    def post(self, request, *args, **kwargs):
        """
        This method checks if the user is authenticated and then calls the POST to get the form information.
        After this it checks if the form is valid and then returns the form.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        if not request.user.is_authenticated:

            return HttpResponseForbidden()

        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():

            return self.form_valid(form)

        else:

            return self.form_invalid(form)



    def form_valid(self, form):
        """
        This method sets the thread user and message from the form data and creates the chat object

        :param form:
        :return:
        """

        thread = self.get_object()

        user = self.request.user

        message = form.cleaned_data.get("message")

        ChatMessage.objects.create(user=user, thread=thread, message=message)

        return super().form_valid(form)