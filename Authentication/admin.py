from django.contrib import admin
from .models import Family, Member
from logged.models import Event

# Register your models here.
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Event)