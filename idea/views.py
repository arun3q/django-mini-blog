from django.shortcuts import render
from .models import Idea




def home(request):
	context = {
		'posts': Idea.objects.all()
	}
	return render(request, "idea/home.html", context)

def about(request):
	return render(request, "idea/about.html", {'title': "About"})