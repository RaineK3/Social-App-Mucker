from django.shortcuts import render,redirect
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm
from django.contrib.auth import authenticate, login, logout

def home(request):
	if request.user.is_authenticated:
		form = MeepForm(request.POST or None)
		if request.method == "POST":
			if form.is_valid():
				meep = form.save(commit = False)
				meep.user = request.user
				meep.save()

				messages.success(request,("Your meep has been posted."))
				return redirect('home')

		meeps = Meep.objects.all().order_by('-created_at')
		return render(request,'home.html', 
			{'meeps': meeps,
			'form':form})
	else:
		meeps = Meep.objects.all().order_by('-created_at')
		return render(request,'home.html', {'meeps': meeps})
def profile_list(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.exclude(user = request.user)
		return render(request, 'profile_list.html',
			{"profiles": profiles})
	else:
		messages.success(request,("You must be logged in to view this page.."))
		return redirect('home')

def profile(request,pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user_id=pk)
		#get the Meep by user id
		meeps = Meep.objects.filter(user_id=pk)
		#post form logic
		if request.method == 'POST':
			#GET current user 
			current_user_profile = request.user.profile
			#get form data
			action = request.POST['follow']
			#decide whether follow or unfollow
			if action == "unfollow":
				current_user_profile.follows.remove(profile)
			elif action == "follow":
				current_user_profile.follows.add(profile)
			#save the profile
			current_user_profile.save()
		return render(request, "profile.html",
			{'profile': profile,
			"meeps": meeps})
	else:
		messages.success(request,("You must be logged in to view this page.."))
		return redirect('home')

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			messages.success(request,("You have been logged in successfully!"))
			return redirect('home')
		else:
			messages.success(request,("There was an error while loggin in. Try agin.."))
			return render(request,"login.html",{})
	else:
		return render(request, "login.html", {})

def logout_user(request):
	logout(request)
	messages.success(request,("You have been logged out."))
	return redirect('home')