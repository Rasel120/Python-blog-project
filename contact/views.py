from django.shortcuts import render
from django.http import HttpResponse
from .models import contact, information, sliders
from django.contrib import messages
from about.models import about_mod
# from pprint import pprint

# Create your views here.
def index(request):
	all_slider = sliders.objects.all()
	data = {
	'slidershow':all_slider
	}
	return render(request, 'index.html', data)

def contact_view(request):
	#message sent/insert part
	if request.method == 'POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		description=request.POST.get('description')

		contact_data= contact(name = name, email = email, subject= subject, description = description)
		contact_data.save()
		messages.success(request, "Your has been submitted!")
		
	#information views part
	all_data = information.objects.all()[0]
	data={
		'inform':all_data	
	}

	return render(request, 'contact.html', data)


def services(request):
	# evabe oo template call kora jay
	template_name = 'services.html'
	return render(request, template_name)

def portfolio(request):
	return render(request, 'portfolio.html')

def slider(request):
	return render(request, 'blog.html')

def search(request):
	allPost = about_mod.objects.all()
	# query_data = request.GET['queres']
	# allPost = about_mod.object.filter(title__icontains=query_data)
	data = {
		'searchresult':allPost}

	return render(request, 'search.html', data)

