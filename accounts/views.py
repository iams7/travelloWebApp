from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from travello.models import Destination


# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.error(request,'Invalid Credentials!')
			return redirect('login')
	else:
		return render (request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('index')

def homepage(request):
	return redirect('index')

def aboutus(request):
	return render (request, 'aboutus.html')

def destination(request):
	dest = Destination.objects.all()
	print (dest)
	return render (request, 'destination.html',{'dest':dest})

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username = username).exists():
				messages.info(request,'Username already taken!')
				return redirect('register')
			elif User.objects.filter(email = email).exists():
				messages.info(request,'Email already taken!')
				return redirect('register')
			else:
				user = User.objects.create_user(
					username=username, 
					first_name=first_name,
					last_name=last_name,
					password = password1,
					email = email
					)
				user.save()
				messages.info(request,'Account created!')
				#return redirect('index')
				return redirect('login')
		else:
			messages.info(request,'Password Mismatched')
			return redirect('register')
	else:
		return render (request, 'register.html')

def contact(request):
	return render (request, 'contact.html')