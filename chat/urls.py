from django.urls import path, re_path
from .views import ThreadView, InboxView
from django.conf.urls import url

app_name = 'chat'

urlpatterns = [

    url(r'^$', InboxView.as_view()),

    url(r'^(?P<username>[^/]+)/$', ThreadView.as_view()),

]

# chat/urls.py
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
"""