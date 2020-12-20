from django.contrib import admin

from .models import Wish
from .models import Ticket


admin.site.register(Wish)
admin.site.register(Ticket)
