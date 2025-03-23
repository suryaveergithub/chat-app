from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sender/<str:room_name>/<str:username>/', views.sender, name='sender'),
    path('receiver/<str:room_name>/<str:username>/', views.receiver, name='receiver'),
]
