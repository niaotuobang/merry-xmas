from django.db import models
from django.contrib.auth.models import User


class Wish(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    wish_from = models.ForeignKey(User, related_name='wish_from', null=True, on_delete=models.SET_NULL)
    wish_gift = models.TextField()
    prepare_gift = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(User, related_name='sender', null=True, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, related_name='receiver', null=True, on_delete=models.SET_NULL)
    address = models.TextField()
    tracking_no = models.CharField(max_length=200)
    received = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
