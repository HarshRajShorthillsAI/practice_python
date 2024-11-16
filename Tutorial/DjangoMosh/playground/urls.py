from django.urls import *
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello)
]