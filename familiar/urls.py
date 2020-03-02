"""familiar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Authentication.views import Home
from Authentication.views import Createuser
from Authentication.views import Loginuser
from Authentication.views import Logedin
from Authentication.views import Logoutuser
from Authentication.views import Createfamily
from Authentication.views import Joinfamily
from Authentication.views import Myfamilies
from Authentication.views import Profile


urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #Home page
    path('', Home, name='home'),
    #AUTHENTICATION
    #Create user
    path('creatuser/', Createuser, name='createuser'),
    #Login
    path('login/', Loginuser, name='loginuser'),
    #Logedin
    path('loggedin/', Logedin, name='logedin'),
    #Logout
    path('logoutuser/', Logoutuser, name='logoutuser'),
    # Create Family
    path('loggedin/createfamily/', Createfamily, name='createfamily'),
    # Join Family
    path('loggedin/joinfamily/', Joinfamily, name='joinfamily'),
    # My families
    path('loggedin/myfamilies/', Myfamilies, name='myfamilies'),
    # Profiles
    path('loggedin/profile/<str:profile_name>', Profile, name='profile'),
    ## CREATE EVENT
    path('main/', include('logged.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)