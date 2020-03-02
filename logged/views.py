from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Event, Photo
from .forms import ImageForm

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

@login_required
def Photos(request):
    if request.method=='GET':
        user = request.user.username
        photos = Photo.objects.filter(author=user)
        return render(request, 'logged/photos.html', {'photos':photos, 'img_form':ImageForm()})

    elif request.method == 'POST':
        if request.POST.get('form_type') == 'delete_photo':
            photo_to_delete = get_object_or_404(Photo, pk=request.POST['photo_id'])
            if photo_to_delete.author == request.user.username:
                photo_to_delete.delete()
            return redirect('photos')
        elif request.POST.get('form_type') == 'add_photo':
            author = request.user.username
            title = request.POST['title']
            desc = request.POST['desc']
            photo = request.FILES['photo_file']

            new_photo = Photo(author=author, title=title,desc=desc, photo=photo)
            #zrobić is valid!
            new_photo.save()

            return redirect('photos')

