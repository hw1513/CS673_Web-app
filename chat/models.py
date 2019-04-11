from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Q

class ThreadManager(models.Manager):
    """
    This class is responsible for managing the threads that are created
    and implements lookups of those threads
    """

    def by_user(self, user):
        """
        Not sure what this method does

        :param user:
        :return:
        """

        # TODO: Rename variables to be easier to understand

        qlookup = Q(first=user) | Q(second=user)

        qlookup2 = Q(first=user) & Q(second=user)

        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()

        return qs



    def get_or_new(self, user, other_username):
        """
        Not sure what this method does

        My assumption is that it gets a new thread for the users

        :param user:
        :param other_username:
        :return:
        """

        username = user.username

        if username == other_username:

            return None

        qlookup1 = Q(first__username=username) & Q(second__username=other_username)

        qlookup2 = Q(first__username=other_username) & Q(second__username=username)

        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()

        if qs.count() == 1:

            return qs.first(), False

        elif qs.count() > 1:

            return qs.order_by('timestamp').first(), False

        else:

            Klass = user.__class__

            user2 = Klass.objects.get(username=other_username)

            if user != user2:

                obj = self.model(

                        first=user, 

                        second=user2

                    )

                obj.save()

                return obj, True

            return None, False


class Thread(models.Model):
    """
    This class initializes the thread and ForeignKey
    of the first and second chat thread. It also holds the value for the timestamp
    """

    first        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_first')

    second       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_second')

    updated      = models.DateTimeField(auto_now=True)

    timestamp    = models.DateTimeField(auto_now_add=True)

    

    objects      = ThreadManager()


    # TODO What does this property decorator do?

    @property

    def room_group_name(self):
        """
        This method is a room_group_name getter method

        :return:
        """

        return f'chat_{self.id}'



    def broadcast(self, msg=None):
        """
        This method broadcasts the message of the user
        to the room group name

        :param msg:
        :return:
        """

        if msg is not None:

            #TODO: I think this is defaulting to admin user, this method doesn't take in user how does that get overrode

            broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')

            return True

        return False





class ChatMessage(models.Model):
    """
    This class initializes the chat message, user and thread
    of the first and second chat thread. It also holds the value for the timestamp
    """

    thread      = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.SET_NULL)

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='sender', on_delete=models.CASCADE)

    message     = models.TextField()

    timestamp   = models.DateTimeField(auto_now_add=True)