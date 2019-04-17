# chat/routing.py
from django.conf.urls import url

from . import consumers


"""
This sets up the pathing for the user chatroom for one on one chats
"""

websocket_urlpatterns = [
    url(r'^messages/(?P<username>[\w.@+-]+)/$', consumers.ChatConsumer),
]


#url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),