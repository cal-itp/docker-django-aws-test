from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("echo/<str:q>", views.echo),
    path("search/<str:q>", views.search)
]
