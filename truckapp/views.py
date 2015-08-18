from django.shortcuts import render, redirect
from django.http import HttpResponse
from truckapp.models import UserInfo, Company, Result
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.db.models import Q
import requests

def homepage(request):
	return render(request, 'home.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def register(request):
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	email = request.POST.get('email')
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = User.objects.create_user(username, email, password)
	user.save()
	print "All users",User.objects.all()
	return redirect('/')

def login_user(request):
	user = User.objects.all().last()
	return render(request, 'login.html', {})

def login_auth(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			login(request,user )
			return redirect('/')
		else:
			return redirect('/signup/')
	else:
		return redirect('/signup/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def questionnaire(request):
	return render(request, 'questionnaire.html', {})

def results(request):
	all_co = Company.objects.all()
	ui = UserInfo()
	ui.experience = request.POST.get("experience")
	ui.salary = request.POST.get("salary")
	ui.otr = request.POST.get("otr")
	ui.regional = request.POST.get("regional")
	ui.dedicated = request.POST.get("dedicated")
	ui.local = request.POST.get("local")
	ui.intermodal = request.POST.get("intermodal")
	ui.bulk	= request.POST.get("bulk")
	ui.solo = request.POST.get("solo")
	ui.team = request.POST.get("team")
	ui.ownerop = request.POST.get("ownerop")
	ui.freight = request.POST.get("freight")
	ui.van = request.POST.get("van")
	ui.flatbed = request.POST.get("flatbed")
	ui.tanker = request.POST.get("tanker")
	ui.elogs = request.POST.get("elogs")
	ui.none = request.POST.get("none")
	ui.hazmat = request.POST.get("hazmat")
	ui.doubles = request.POST.get("doubles")
	ui.xtanker = request.POST.get("xtanker")
	ui.miles = request.POST.get("mileage")
	ui.med = request.POST.get("med")
	ui.dental = request.POST.get("dental")
	ui.vision = request.POST.get("vision")
	ui.life = request.POST.get("life")
	ui.pets = request.POST.get("pets")
	ui.riders = request.POST.get("riders")
	ui.save()

	experience = {"1":(0,2),"2":(0,6),"3":(0,12),"4":(0,24),"5":(0,36),"6":(0,100)}
	salary = {"1":(30000,39999),"2":(40000,49999),"3":(50000,59999),"4":(60000,69999),"5":(70000,79999),"6":(80000,1000000),"7":(30000,1000000),}
	dr_type = ["solo","team","ownerop"]
	if ui.experience in experience and ui.salary in salary: 
		print "***********", ui.experience,ui.salary
		if ui.solo in dr_type:
			print "***********",ui.solo
			results = Company.objects.filter(experience__gte=experience[ui.experience][0],experience__lte=experience[ui.experience][1], salary__gte=salary[ui.salary][0],salary__lte=salary[ui.salary][1],driver_type=dr_type[0])
			if results:
				return render(request, 'results.html', {"all_companies":results})
			else:
				return render(request, 'no_results.html', {})
		elif ui.team in dr_type:
			results = Company.objects.filter(experience__gte=experience[ui.experience][0],experience__lte=experience[ui.experience][1], salary__gte=salary[ui.salary][0],salary__lte=salary[ui.salary][1],driver_type=dr_type[1])
			if results:
				return render(request, 'results.html', {"all_companies":results})
			else:
				return render(request, 'no_results.html', {})
		elif ui.ownerop in dr_type:
			results = Company.objects.filter(experience__gte=experience[ui.experience][0],experience__lte=experience[ui.experience][1], salary__gte=salary[ui.salary][0],salary__lte=salary[ui.salary][1],driver_type=dr_type[2])
			if results:
				return render(request, 'results.html', {"all_companies":results})
			else:
				return render(request, 'no_results.html', {}) 
	else:
		return render(request, 'results.html', {"all_companies":all_co})

def co_contact(request):
	return render(request, 'home.html', {})

def co_profile(request):
	return render(request, 'home.html', {})

def links(request):
	return render(request, 'links.html', {})

def search(request):
	company = Company.objects.all()
	if request.GET.get('search'):
		search = request.GET.get('search')
		company = Company.objects.filter(Q(name__icontains=search))
		return render(request, 'search.html', {"company":company})
	else:
		return redirect('/links/')

def zip_form(request):
	return render(request, 'zip_form.html', {})

def distance(request):
	distance_url = "https://redline-redline-zipcode.p.mashape.com/rest/distance.json/"
	zip1 = request.POST.get('zip1')
	zip2 = request.POST.get('zip2')
	distance_url += zip1 + '/' + zip2 + '/mile'
	response = requests.post(distance_url, headers={'X-Mashape-Key': '4EpPEDWTYYmshsizWRGCH8w71C6Gp1wiPHajsn4VIx5gu8XRAC','Accept': 'application/json'
                      })
	result = response.content
	numbers = []
	yes = ['1','2','3','4','5','6','7','8','9','0',',','.']
	try:
		for char in result:
			if char in yes:
				numbers.append(char)
			else:
				print "Oops, please enter a valid Zip Code."
		result = ''.join(numbers)
		print '********',result
		return render(request, 'distance.html', {'zip1':zip1,'zip2':zip2,'distance':result})

	except :
		print "Oops, please enter a valid Zip Code."

def weather_form(request):
	return render(request, 'weather_form.html', {})