from django.urls import path
from django.conf.urls import url
from . import views
from chat.views import ThreadView, InboxView


"""
This file configures the routing and paths that Django
will serve for our functionality
"""
urlpatterns = [

    path('', views.login_user, name='home'),
    path('<operation>/<int:pk>/', views.change_friends, name='change_friends'),

    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('issue/', views.issue, name='issue'),

    path('friend/', views.friend, name='friend'),
    url(r'^friend/(?P<username>[^/]+)/$', ThreadView.as_view(), name='start_chat'),

]
