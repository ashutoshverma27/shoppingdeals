from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.compare,name='compare'),
    path('add/',views.add,name='add'),
    path('added/',views.added,name='added'),
]
