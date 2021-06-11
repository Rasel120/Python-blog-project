from django.shortcuts import render
from .models import endfooter

# Create your views here.

def index(request):
	all_data = endfooter.objects.all()[0]
	data = {
		'end_footer':all_data
	}
	return render(request, 'footer.html', data)