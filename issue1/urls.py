from django.urls import path
from . import views

urlpatterns = [
	path('', views.issue_home, name='issue_home'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('cross_off/<list_id>', views.cross_off, name='cross_off'),
	path('uncross/<list_id>', views.uncross, name='uncross'),
	path('edit/<list_id>', views.edit, name='edit'),
	path('addnew/', views.addnew, name='addnew'), 

]
    
