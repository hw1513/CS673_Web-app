from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo_home, name='todo_home'),
	path('delete/<list_id>', views.delete1, name='delete1'),
	path('cross_off/<list_id>', views.cross_off1, name='cross_off1'),
	path('uncross/<list_id>', views.uncross1, name='uncross1'),
	path('detail/<list_id>', views.detail, name='idetail'),
	path('edit/<list_id>', views.edit, name='iedit'),
	path('addnew_item/', views.addnew_item, name='addnew_item'), 

]
    
