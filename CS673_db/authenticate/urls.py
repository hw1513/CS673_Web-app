from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

	
	path('', views.login_user, name='home'),
	path('<operation>/<int:pk>/', views.change_friends, name='change_friends'),
	
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('change_password/', views.change_password, name='change_password'),
	path('program/', views.program, name='program'),
	path('issue/', views.issue, name='issue'),
	path('friend/', views.friend, name='friend'),

]
