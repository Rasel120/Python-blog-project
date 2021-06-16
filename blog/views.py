from django.shortcuts import render
from .models import blog
from django.contrib import messages

# Create your views here.

def blogs(request):
	# [:4] This is range count
	all_data = blog.objects.all()[:4]
	data={
		'blog_all':all_data	
	}
	return render(request,'blog.html', data)


def search(request):
	# allPost = blog.objects.all()
	query_data = request.GET['queres']
	allPost = blog.objects.filter(title__icontains=query_data)
	params = {
		'searchresult':allPost}

	return render(request, 'search.html', params)

