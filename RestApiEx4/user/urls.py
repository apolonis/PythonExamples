from django.urls import path

from . import views

# This is like mapping in java
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
]
