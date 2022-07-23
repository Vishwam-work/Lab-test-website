"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),
    path('contact/', views.contact,name='contact'),
    path('health/', views.health,name='health'),
    path('choice/', views.choice,name='choice'),
    path('choice1/', views.choice1,name='choice1'),
    path('sample/',views.sample,name='sample'),
    path('',include('adminapp.urls')),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    

    
]

