from django.urls import path, re_path
from .views import ThreadView, InboxView
from django.conf.urls import url


app_name = 'chat'

urlpatterns = [

    url(r'^$', InboxView.as_view()),

    url(r'^(?P<username>[^/]+)/$', ThreadView.as_view(),),

]

