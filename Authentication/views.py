from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Family, Member
from .forms import CreateFamily
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
        error = 'Wrong username or password. Please try again.'
        return render(request, 'Authentication/loginuser.html', {'form': AuthenticationForm(), 'error':error})

@login_required
def Logedin(request):
    families = Family.objects.filter()
    my_families = [] # ffamilies that I belong to
    for family in families:
        for member in family.members.all():
            if str(member) == str(request.user.username):
                my_families.append(family)

    return render(request, 'Authentication/logedin.html', {'families': families,'my_families':my_families})


@login_required
def Logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

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
        newfamily.members.add(new_member)

        return redirect('logedin')

@login_required
def Joinfamily(request):
    if request.method == 'GET':
        return render(request, 'Authentication/joinfamily.html')
    elif request.method == 'POST':
        member = request.user.username
        try:
            new_member = get_object_or_404(Member, member=member)
        except:
            new_member = Member(member=member)
            new_member.save()

        pk = request.POST['family_id']
        family = get_object_or_404(Family, pk=pk)
        family.members.add(new_member)
        family.save()

        return redirect('logedin')
