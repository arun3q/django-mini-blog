from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="idea-home"),
	path("about/", views.about, name="idea-about"),
]