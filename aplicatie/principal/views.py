from django.shortcuts import render

def index(request):
	return render(request, 'principal/index.html')

def contact(request):
	return render(request, 'principal/contact.html')
