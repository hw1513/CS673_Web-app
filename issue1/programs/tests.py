from django.test import TestCase
from programs.models import Programs
# Create your tests here.
from django.contrib.auth.models import User

class ProgramsModelTest(TestCase):
  @classmethod
  def setUpTestData(self):
    Programs.objects.create(project_name='test01')
   
  def test_project_name_label(self):
    programs=Programs.objects.get(id=1)
    field_label = author._meta.get_field('project_name').verbose_name
    self.assertEquals(field_label,'project_name')
    
  def test_start_date_label(self):
    programs=Programs.objects.get(id=1)
    field_label = author._meta.get_field('start_date').verbose_name
    self.assertEquals(field_label,'start_date')
    
  def test_first_name_max_length(self):
    programs=Programs.objects.get(id=1)
    max_length = programs._meta.get_field('project_name').max_length
    self.assertEquals(max_length,20)
    

