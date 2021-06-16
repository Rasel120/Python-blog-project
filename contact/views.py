from django.shortcuts import render
from .models import contact, information
from django.contrib import messages
# Create your views here.

def contact_view(request):
	#message sent/insert part
	if request.method == 'POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		description=request.POST.get('description')

		contact_data= contact(name = name, email = email, subject= subject, description = description)
		contact_data.save()
		messages.success(request, "Your message has been submitted!")
		
	#information views part
	all_data = information.objects.all()[0]
	data={
		'inform':all_data	
	}

	return render(request, 'contact.html', data)

