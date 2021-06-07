from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('homepage', views.homepage),
    path("login", views.register),
    path("user-login", views.user_login),
    path('logout/', views.logoutUser),
    path('add-meal', views.Add_meal),
    # path('delete-meal', views.delete_meal),
    path('add-profile', views.add_profile),
    # path(profile/'<int:user_id>'/edit , views.edit_profile),
    path('nav', views.nav)
    
]
