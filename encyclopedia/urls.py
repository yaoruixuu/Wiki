from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("Random", views.Random, name="Random"),
    path("<str:entry>", views.entry, name="entry")
    
    
]
