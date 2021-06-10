from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('user-profile', views.User_Profile),
    path("login", views.register),
    path("user-login", views.user_login),
    path('logout/', views.logoutUser),
    path('add-meal', views.Add_meal),
    path('user-dashboard', views.Dashboard),
    path('add-profile', views.add_profile),
    path('delete/<int:id>', views.delete),
    path('blog', views.blog),
    path('add-blog', views.add_blog),
    path('edit/<int:blog_id>', views.edit_blog),
    path('modify-blog', views.modify_blog),
    path('delete/<int:blog_id>', views.delete_blog),
    path('add-comment', views.add_comment)
    
]
