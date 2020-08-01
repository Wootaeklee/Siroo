from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('sign_up_start/', views.sign_up_start, name='sign_up_start'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up_profile/', views.sign_up_profile, name='sign_up_profile'),
    path('sign_up_tags/', views.sign_up_tags, name='sign_up_tags'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>new_profile/', views.new_profile, name='new_profile'),
    path('<int:user_id>/update_profile/', views.update_profile, name='update_profile'),
]