from django.shortcuts import render
from .models import about_mod
from pprint import pprint

# Create your views here.

def aboutdata(request):	
	ab_data = about_mod.objects.all()[0]
	contex={
		'abou_all':ab_data	
	}
	return render(request,'about.html', contex)

# def ourteam(request):
