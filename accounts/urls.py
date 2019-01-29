from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import login,logout
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
app_name = "accounts"

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('data/',views.showall,name='showall'),
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.view_profile,name='view_profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_password'),
    
    re_path( r'delete/(?P<pk>\d+)/$', views.tasdelevie.as_view(template_name="accounts/delete.html"),name='delete'),

]
