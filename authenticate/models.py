from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    """
    This class initializes the friend functionality
    which includes adding and removing friends
    """
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    # TODO: Charlie can we go over how thee class method decorators work?

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
