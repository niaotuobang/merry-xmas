from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Wish
from .models import Ticket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class WishSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Wish
        fields = '__all__'
        read_only_fields = ('id', 'author')


class TicketSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Ticket
        fields = '__all__'
