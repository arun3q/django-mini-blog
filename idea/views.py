from django.shortcuts import render


posts = [
	{
		'author': "Arun",
		'title': "Idea one",
		'content': "My first idea just to test the app.",
		'date_posted': 'September 1, 2018'
	},
	{
		'author': "Avinash",
		'title': "Idea Two",
		'content': "My Second idea just to test the app.",
		'date_posted': 'September 1, 2018'
	},
	{
		'author': "Amit",
		'title': "Idea second",
		'content': "My 3rd idea just to test the app.",
		'date_posted': 'September 1, 2018'
	},
]



def home(request):
	context = {
		'posts': posts
	}
	return render(request, "idea/home.html", context)

def about(request):
	return render(request, "idea/about.html", {'title': "About"})