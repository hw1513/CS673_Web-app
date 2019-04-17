# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^messages/(?P<username>[\w.@+-]+)/$', consumers.ChatConsumer),
]


#url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),