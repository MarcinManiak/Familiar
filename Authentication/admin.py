from django.contrib import admin
from .models import Family, Member
from logged.models import Event, Post, Comment

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)