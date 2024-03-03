from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyJsonView.as_view(), name="index"),
]