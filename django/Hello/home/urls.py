from django.contrib import admin
from django.urls import path,include 
from home import views


urlpatterns = [

    path("register",views.registerPage,name='regsiter'),

    path("login",views.loginPage,name='login'),
    
    path("logout",views.logoutUser,name='logout'),
    
    path("",views.index,name='home'),
    
    path("about",views.about,name='about'),
    
    path("services",views.services,name='services'),

    path("techno_event", views.techno_event, name='techno_event'),

    path("parties", views.parties, name='parties'),

    path("college", views.college, name='college'),

    path("contact",views.contact,name='contact'),

    path("profile",views.profile,name='profile'),
   
    
]