from django.shortcuts import render

from articol.models import Category, Articol

def index(request):
	articole = Articol.objects.filter(is_sold=False)[0:6]
	Marci = Category.objects.all()

	return render(request, 'principal/index.html',{
		'Marci': Category,
		'articole': articole,
	})

def contact(request):
	return render(request, 'principal/contact.html')
