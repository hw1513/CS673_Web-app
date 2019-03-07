from django.urls import path
from . import views


urlpatterns = [
	path('', views.program),
	path('<program_name>/', views.detail, name='detail'),

	
	

]
