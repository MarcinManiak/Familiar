from django.urls import path, include
from .views import Addevent, Myevents


urlpatterns = [
    #Add event
    path('addevent/', Addevent, name='addevent'),
    path('myevents/', Myevents, name='myevents'),
]
