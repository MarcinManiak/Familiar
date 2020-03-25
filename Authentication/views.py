import random
import string
import datetime
from operator import attrgetter
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Family, Member
from .forms import CreateFamily
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission
from logged.models import Event, Post, Photo, Comment



# Create your views here.
def Home(request):
    return render(request, 'Authentication/home.html')

def Createuser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            permission = Permission.objects.get(name='Can view user')
            user.user_permissions.add(permission)
            login(request, user)
            return redirect('logedin')
    else:
        form = SignUpForm()
    return render(request, 'Authentication/createuser.html', {'form': form})

def Loginuser(request):
    if request.method == 'GET':
        return render(request, 'Authentication/loginuser.html', {'form': AuthenticationForm()})
    try:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
            login(request, user)
            return redirect('logedin')
    except:
        error = 'Niepoprawne dane. Spróbuj jeszcze raz!'
        return render(request, 'Authentication/loginuser.html', {'form': AuthenticationForm(), 'error':error})

@login_required
def Logedin(request):
    if request.method == 'GET':
        families = Family.objects.filter()
        my_families = [] # families that I belong to
        events = Event.objects.all()# all database events
        members_of_my_families = []
        events_in_my_families = []

        for family in families:
            for member in family.members.all():
                if str(member) == str(request.user.username):
                    my_families.append(family)

        for family in my_families:
            for member in family.members.all():
                members_of_my_families.append(member.member)

        members_of_my_families = list(dict.fromkeys(members_of_my_families))

        for event in events:
            if event.author in members_of_my_families:
                events_in_my_families.append(event)

        events_in_my_families = list(dict.fromkeys(events_in_my_families))

        for event_in_family in events_in_my_families:
            if event_in_family.month < datetime.datetime.now().month:
                event_in_family.this_year = datetime.datetime(datetime.datetime.now().year + 1, event_in_family.month,
                                                              event_in_family.month)
            elif event_in_family.month > datetime.datetime.now().month:
                event_in_family.this_year = datetime.datetime(datetime.datetime.now().year,
                                                              event_in_family.month,
                                                              event_in_family.month)
            else:
                if event_in_family.day < datetime.datetime.now().day:
                    event_in_family.this_year = datetime.datetime(datetime.datetime.now().year + 1,
                                                                  event_in_family.month,
                                                                  event_in_family.month)
                else:
                    event_in_family.this_year = datetime.datetime(datetime.datetime.now().year,
                                                                  event_in_family.month,
                                                                  event_in_family.month)

        sorted_events = sorted(events_in_my_families, key=attrgetter('this_year'))
        two_events = sorted_events.copy()[:3]
        how_much_events = len(sorted_events)


        posts = Post.objects.all().order_by('-date') #all posts
        posts_in_my_families = []

        comments = Comment.objects.all().order_by('-date')
        comments_in_my_families = []

        for post in posts:
            if post.author in members_of_my_families:
                posts_in_my_families.append(post)

        for comment in comments:
            if comment.author in members_of_my_families:
                comments_in_my_families.append(comment)

        posts_in_my_families = list(dict.fromkeys(posts_in_my_families))
        comments_in_my_families = list(dict.fromkeys(comments_in_my_families))

        try:
            latest_post = posts_in_my_families[0]
        except:
            latest_post = None

        photos = Photo.objects.all().order_by('-date')  # all photos
        photos_in_my_families = []

        for photo in photos:
            if photo.author in members_of_my_families:
                photos_in_my_families.append(photo)

        photos_in_my_families = list(dict.fromkeys(photos_in_my_families))
        try:
            latest_photo = photos_in_my_families[0]
        except:
            latest_photo = None;


        return render(request, 'Authentication/loggedin.html',{'my_families':my_families, 'events_in_my_families':sorted_events, 'members_of_my_families':members_of_my_families,'posts_in_my_families':posts_in_my_families,'photos_in_my_families':photos_in_my_families,'comments_in_my_families':comments_in_my_families,'two_events':two_events,'how_much_events':how_much_events,'latest_post':latest_post,'latest_photo':latest_photo})

    elif request.method == 'POST':
        if request.POST.get("form_type") == 'post':
            user = request.user.username
            post = request.POST['send_post']
            if post != '':
                new_post = Post(text=post, author=user)
                new_post.save()

            return redirect('logedin')

        if request.POST.get("form_type") == 'delete':
            post_to_delete = get_object_or_404(Post, pk=request.POST['post_to_delete'])
            if post_to_delete.author == request.user.username:
                post_to_delete.delete()
            return redirect('logedin')

        if request.POST.get("form_type") == 'form_comment':
            user = request.user.username
            comment = request.POST['comment']
            pk_post = request.POST['commented_post']
            post = get_object_or_404(Post, pk=pk_post)

            if comment != '':
                new_comment = Comment(author=user, text=comment, post=post)
                new_comment.save()

            return redirect('logedin')


        if request.POST.get("form_type") == 'form_comment_delete':
            pk_comment = request.POST['delete_comment']
            comment = get_object_or_404(Comment, pk=pk_comment)
            if comment.author == request.user.username:
                comment.delete()

            return redirect('logedin')




@login_required
def Logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@login_required
def Createfamily(request):
    if request.method == 'GET':
        return render(request, 'Authentication/createfamily.html', {'form': CreateFamily()})
    elif request.method == 'POST':
        member = request.user.username
        try:
            new_member = get_object_or_404(Member, member=member)
        except:
            new_member = Member(member=member)
            new_member.save()

        name = request.POST['name']
        description = request.POST['description']
        newfamily = Family(name=name, description=description)
        newfamily.save()


        newfamily.password = str(randomStringDigits(4)+str(int((int(newfamily.pk)*3-2)/2)))
        newfamily.save()
        newfamily.members.add(new_member)

        return redirect('myfamilies')

@login_required
def Joinfamily(request):
    error = None;
    if request.method == 'GET':
        return render(request, 'Authentication/joinfamily.html',{"error":error})
    elif request.method == 'POST':
        member = request.user.username
        try:
            new_member = get_object_or_404(Member, member=member)
        except:
            new_member = Member(member=member)
            new_member.save()

        password = request.POST['family_id']
        try:
            family = get_object_or_404(Family, password=password)
        except:
            error='Rodzina o podanym ID nie istnieje.'
            return render(request, 'Authentication/joinfamily.html',{"error":error})
        family.members.add(new_member)
        family.save()

        return redirect('myfamilies')

@login_required
def Myfamilies(request):
    if request.method=='GET':
        families = Family.objects.filter()
        my_families = [] # families that I belong to
        number_of_families = 0 #Number of families user belongs
        for family in families:
            for member in family.members.all():
                if str(member) == str(request.user.username):
                    my_families.append(family)
        number_of_families = len(my_families)
        return render(request, 'Authentication/myfamilies.html', {'my_families':my_families,'number_of_families':number_of_families})
    elif request.method == 'POST':
        member = request.user.username
        new_member = get_object_or_404(Member, member=member)

        family_id = request.POST['family_id']
        family = get_object_or_404(Family, pk=family_id)
        family.members.remove(new_member)
        family.save()

        return redirect('myfamilies')

@login_required
def Profile(request, profile_name):
    profile = get_object_or_404(User, username=profile_name)
    return render(request, 'Authentication/profile.html', {'profile':profile})