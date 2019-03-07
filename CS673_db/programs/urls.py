from django.urls import path
from . import views


urlpatterns = [
	path('', views.program),
	path('<program_name>/', views.detail, name='detail'),
	path('<program_name>/add_member/', views.add_member, name='add_member')

	
	

]
