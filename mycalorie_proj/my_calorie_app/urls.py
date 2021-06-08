from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('User-Profile', views.User_Profile),
    path("login", views.register),
    path("user-login", views.user_login),
    path('logout/', views.logoutUser),
    path('add-meal', views.Add_meal),
    path('user-dashboard', views.Dashboard),
    # path('delete-meal', views.delete_meal),
    path('add-profile', views.add_profile),
    # path(profile/'<int:user_id>'/edit , views.edit_profile),
    # path('nav', views.nav),
    path('delete/<int:id>' , views.delete),
    
]
