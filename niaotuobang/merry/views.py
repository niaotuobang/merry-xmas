import random

from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Wish
from .models import Ticket

from .serializers import UserSerializer
from .serializers import WishSerializer
from .serializers import TicketSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class FetchTicketView(APIView):
    def post(self, request):
        if not request.user:
            raise serializers.ValidationError('请登录后操作')

        users = User.objects.all()
        tickets = Ticket.objects.all()
        wishes = Wish.objects.all()
        '''
        has_write = False
        for wish in wishes:
            if wish.author.id == request.user.id:
                has_write = True
        if not has_write:
            raise serializers.ValidationError('请填写愿望')

        if len(wishes) != len(ticket):
            raise serializers.ValidationError('等待其他参与用户填写愿望')
        '''

        # TODO add lock
        has_send_ticket_user_map = {}
        for ticket in tickets:
            has_send_ticket_user_map[ticket.sender.id] = True
            if ticket.receiver.id == request.user.id:
                serializer = TicketSerializer(ticket, context={'request': request})
                return Response(serializer.data)

        candidates = []
        for user in users:
            if user.id == request.user.id:
                continue
            if user.id in has_send_ticket_user_map:
                continue
            candidates.append(user)

        sender = random.choice(candidates)

        ticket = Ticket(
            sender=sender,
            receiver=request.user,
            address='请私聊',
            tracking_no='',
            received=False)
        ticket.save()

        serializer = TicketSerializer(ticket, context={'request': request})
        return Response(serializer.data)
