import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        """
        This method creates the websocket connection between two users async.
        
        :param event: 
        :return: 
        """"
        print('connected', event)
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        #print(other_user, me)
        thread_obj = await self.get_thread(me, other_user)
        self.thread_obj= thread_obj
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )


        await self.send({
            "type" : "websocket.accept"
        })
        #await asyncio.sleep(10)
        
        

    async def websocket_receive(self, event):
        """


        :param self:
        :param event:
        :return:
        """
        # TODO: Change this to using a logger

        print('receive', event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg=loaded_dict_data.get('message')
            user = self.scope['user']
            username = 'default'
            if user.is_authenticated:
                username=user.username

            # TODO: change this to logger
            #print(msg)

            # Builds the response
            myResponse={
                'message' : msg ,
                'username' : username
            }
            await self.create_chat_message(user, msg)

            #broadcasts the message event to be sent
            await self.channel_layer.group_send(
                self.chat_room,
                {
                    "type" : "chat_message" ,
                    "text" : json.dumps(myResponse)
                }
            )

    async def chat_message(self, event):
        """
        This method sends the message as an event

        :param event:
        :return:
        """
        print('message', event)
        await self.send({
                "type" : "websocket.send",
                "text" : event['text']
            })

    async def websocket_disconnect(self, event):
        """
        This method asynchronously allows the user to disconnect

        :param event:
        :return:
        """

        #TODO: This may need to be converted to logger
        print('disconnected', event)

    @database_sync_to_async
    def get_thread(self, user, other_username):
        """
        This method gets the index 0 new object from the thread
        shared by both of the users

        :param user:
        :param other_username:
        :return:
        """
        return Thread.objects.get_or_new(user, other_username)[0]

    @database_sync_to_async
    def create_chat_message(self, me, msg):
        """
        This method is creating the chat message and leveraging the database
        to by creating that based on the thread

        :param me:
        :param msg:
        :return:
        """
        thread_obj = self.thread_obj
        return ChatMessage.objects.create(thread=thread_obj, user=me,  message=msg)

