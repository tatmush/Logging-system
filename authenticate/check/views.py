from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Check
from django.utils import timezone

# Create your views here.
def index(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		entry = Check(user=user, checkOut=None)
		
		entry.save()
		return redirect('index')
	else:
		if request.user.is_authenticated:
			user = User.objects.get(id=request.user.id)
			#get current day's instance and update in the database
			today = timezone.now().date()
			checkObject = Check.objects.filter(user=user).filter(checkIn__gt=today).first()
			context = {}
			if not checkObject:
				#user has not logged in for the day
				context = {
					'state': False
				}
			elif checkObject.checkOut == None and checkObject.checkIn.date()>=today :
				#User has logged in but not logged out for the day
				context = {
					'state': True
				}
			else:
				#user has logged in and logged out for the day
				context = {
					'state': None
				}
			return render(request, 'check/index.html', context)
	return render(request, 'check/index.html')

		

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	context = {'form' : form}
	return render(request, 'registration/register.html', context)

def checkOut(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		#get current day's instance and update in the database
		today = timezone.now().date()
		checkObject = Check.objects.filter(user=user).filter(checkIn__gt=today).first()
		checkObject.checkOut = timezone.now()
		checkObject.save()
		
		return redirect('index')
	else:
		return render(request, 'check/index.html')


