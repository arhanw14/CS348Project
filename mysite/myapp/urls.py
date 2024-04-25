from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("", views.index, name='index'),
    path("add/", views.add, name='add'),
    path("edit/", views.edit, name='edit'),
    path("remove/", views.remove, name='remove'),
    path("filter", views.filter, name='filter')
]