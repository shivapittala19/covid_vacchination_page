from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login_user',views.login_user,name='login'),
    path('logout_user',views.logout_user,name='Logout'),
    path('apply',views.apply,name='apply'),
    path('search',views.search,name='search')
    
]