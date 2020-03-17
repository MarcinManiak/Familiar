from django.urls import path, include
from .views import Addevent, Myevents, Photos, Phonebook


urlpatterns = [
    path('addevent/', Addevent, name='addevent'),
    path('myevents/', Myevents, name='myevents'),
    path('photos/', Photos, name='photos'),
    path('phonebook/', Phonebook, name='phonebook'),
]

