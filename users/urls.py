from . import views
from django.urls import path




urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('other/', views.other, name='other'),
    path('create-profile/',views.create_profile,name='create-profile')
]
