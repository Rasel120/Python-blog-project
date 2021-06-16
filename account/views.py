from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def authlogin(request):
	if request.method == 'POST':
		username = request.POST.get('name')
		password = request.POST.get('password')
		user = authenticate(request, Username = username, Password = password)
		

		if user is not None:
			login(request,user)
			return redirect('/profile/')
		else:
			return messages.error(request, "invalid!")

	return render(request,'authfile/login.html')

	
def authregister(request):
	if request.method == 'POST':		
		username = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')

		#password match check
		if password == password2:
			#username match check from database
			if User.objects.filter(username = username).exists():
				messages.error(request, "Username already exisist")
			#email match check from database
			elif User.objects.filter(email = email).exists():
				messages.error(request, "Email already exisist")
			else:
				user = User.objects.create_user(username = username, email = email, password = password)
				user.save()
				messages.success(request, "Registration Successfully!")
				return redirect('login')
		else:
			messages.error(request, "Password Not Matched")

	return render(request,'authfile/register.html')	


def authforgot(request):
	return render(request,'authfile/forgetpassword.html')


def authprofile(request):
	return render(request,'authfile/profile.html')


def authlogout(request):
	logout(request)
	messages.success(request, "Logout Success!")
	return redirect('login')