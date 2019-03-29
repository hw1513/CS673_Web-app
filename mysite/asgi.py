import os 
import django
from channels.routing import get_defauly_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
application=get_defauly_application()