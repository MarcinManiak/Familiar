from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Event, Photo, Phone
from Authentication.models import Family
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
        author = request.user.username
        my_events = Event.objects.filter(author=author)

        new_event = Event(author=author,occasion=occasion, desc=desc,day=day,month=month)
        new_event.save()
        msg = 'Dodano wydarzenie'

        return render(request, 'logged/myevents.html', {'my_events':my_events,'msg':msg})

@login_required
def Myevents(request):
    if request.method=='GET':
        author = request.user.username
        my_events = Event.objects.filter(author=author)
        msg = False
        return render(request, 'logged/myevents.html', {'my_events':my_events,'msg':msg})
    elif request.method == 'POST':
        author = request.user.username
        my_events = Event.objects.filter(author=author)
        event = request.POST['event_id']
        event_to_delete = get_object_or_404(Event, pk=event)
        event_to_delete.delete()
        msg = 'Wydarzenie usunięto'
        return render(request, 'logged/myevents.html', {'my_events':my_events,'msg':msg})

@login_required
def Photos(request):
    if request.method=='GET':
        user = request.user.username
        photos = Photo.objects.filter(author=user)
        msg=False
        return render(request, 'logged/photos.html', {'photos':photos, 'img_form':ImageForm(),'msg':msg})

    elif request.method == 'POST':
        if request.POST.get('form_type') == 'delete_photo':
            photo_to_delete = get_object_or_404(Photo, pk=request.POST['photo_id'])
            if photo_to_delete.author == request.user.username:
                user = request.user.username
                photos = Photo.objects.filter(author=user)
                photo_to_delete.delete()
                msg = 'Zdjęcie usunięte'

                return render(request, 'logged/photos.html', {'photos':photos, 'img_form':ImageForm(),'msg':msg})

        elif request.POST.get('form_type') == 'add_photo':
            user = request.user.username
            photos = Photo.objects.filter(author=user)
            author = request.user.username
            title = request.POST['title']
            desc = request.POST['desc']
            photo = request.FILES['photo_file']

            new_photo = Photo(author=author, title=title,desc=desc, photo=photo)
            #zrobić is valid!
            new_photo.save()
            msg = 'Zdjęcie dodane - sprawdź na dole strony'

            return render(request, 'logged/photos.html', {'photos':photos, 'img_form':ImageForm(),'msg':msg})

@login_required
def Phonebook(request):
    if request.method=='GET':

        families = Family.objects.filter()
        phone_numbers = Phone.objects.all()
        numbers_in_my_families = []
        my_families = [] # families that I belong to
        members_of_my_families = []

        for family in families:
            for member in family.members.all():
                if str(member) == str(request.user.username):
                    my_families.append(family)

        for family in my_families:
            for member in family.members.all():
                members_of_my_families.append(member.member)

        members_of_my_families = list(dict.fromkeys(members_of_my_families))

        for number in phone_numbers:
            if number.author in members_of_my_families:
                numbers_in_my_families.append(number)

        numbers_in_my_families = list(dict.fromkeys(numbers_in_my_families))

        allow = False
        my_number = None

        for number in numbers_in_my_families:
            if number.author == request.user.username:
                my_number = number.phone_number
                allow = True

        return render(request, 'logged/phonebook.html', {'numbers_in_my_families':numbers_in_my_families, 'allow':allow,'my_number':my_number})

    elif request.method == 'POST':
        author = request.user.username
        phone_number = request.POST['phone_number']
        if request.POST.get('what_to_do') == 'edit_number':
            if request.POST.get('phone_number').isnumeric():
                to_edit = Phone.objects.get(author=author)
                to_edit.phone_number = request.POST.get('phone_number')
                print(to_edit.phone_number)
                print(request.POST.get('phone_number'))
                to_edit.save()
                return redirect('phonebook')
            else:
                return redirect('phonebook')

        elif phone_number.isnumeric():
            try:
                new_number = get_object_or_404(Phone, author=author)
                error = 'Dodałeś już numer telefonu'
                return render(request, 'logged/phonebook.html', {'error': error})
            except:
                new_number = Phone(author=author, phone_number=phone_number)
                new_number.save()
                error = None
                return redirect('phonebook')
        else:
            error = 'Podaj proszę numer złożony wyłącznie z liczb!'
            return render(request, 'logged/phonebook.html', {'error': error})



