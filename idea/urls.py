from django.urls import path
from . import views
from .views import (IdeaListView,
 					IdeaDetailView, 
 					IdeaCreateView, 
 					IdeaUpdateView, 
 					IdeaDeleteView,
 					UserIdeaListView
 					)

urlpatterns = [
	path("", IdeaListView.as_view(), name="idea-home"),
	path("user/<str:username>", UserIdeaListView.as_view(), name="user-ideas"),
	path("idea/<int:pk>/", IdeaDetailView.as_view(), name="idea-detail"),
	path("idea/new/", IdeaCreateView.as_view(), name="idea-create"),
	path("idea/<int:pk>/update/", IdeaUpdateView.as_view(), name="idea-update"),
	path("idea/<int:pk>/delete/", IdeaDeleteView.as_view(), name="idea-delete"),
	path("about/", views.about, name="idea-about"),
]