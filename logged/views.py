from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from Authentication.models import Family, Member
from .models import Event

@login_required
def Addevent(request):
    if request.method == 'GET':
        return render(request, 'logged/addevent.html')
    else:
        author = request.user.username
        occasion = request.POST['occasion']
        desc = request.POST['desc']
        day = request.POST['day']
        month = request.POST['month']

        new_event = Event(author=author,occasion=occasion, desc=desc,day=day,month=month)
        new_event.save()

        return redirect('logedin')

@login_required
def Myevents(request):
    if request.method=='GET':
        author = request.user.username
        my_events = Event.objects.filter(author=author)
        return render(request, 'logged/myevents.html', {'my_events':my_events})
    elif request.method == 'POST':
        event = request.POST['event_id']
        event_to_delete = get_object_or_404(Event, pk=event)
        event_to_delete.delete()

        return redirect('logedin')

