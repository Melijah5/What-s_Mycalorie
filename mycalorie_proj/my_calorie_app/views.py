from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .form import ProfileForm
# from .form import ImageForm
# from .models import Image
from .models import User
from .models import *
import requests
import bcrypt


def index(request):
    return render(request, 'homepage.html')

def register(request):
    errors = User.objects.basic_validation(request.POST)
    # print(request.POST)
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')    
  
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=hash1)
    request.session['loginID']= newuser.id
    return redirect("/homepage")
def homepage(request):
    if 'loginID' not in request.session:
        return redirect('/')
    context = {
        'userlogged': User.objects.get(id = request.session['loginID'])
    }
    return render(request, 'Profile.html', context)

def user_login(request):
    userErrors = User.objects.login_validator(request.POST)
    if len(userErrors) > 0:
        for key,val in userErrors.items():
            messages.error(request,val)
        return redirect('/')
    
    user = User.objects.get(email = request.POST['email'])
    request.session['loginID'] = user.id
    return redirect('/homepage')

def logoutUser(request):
    request.session.clear()
    return redirect("/")

def add_profile(request):
  
    if request.method == 'POST': 
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        # profile_pic = request.POST['profile_pic']
        activity = request.POST['activity']
        
        # BMI = weight / (height/100)**2
        ProfileSetting.objects.create(age=age , gender=gender, height=height, weight=weight,  activity=activity)
        
              

        # print(f"You BMI is {BMI}")

        # if BMI <= 18.4:
        #     print("You are underweight.")
        # elif BMI <= 24.9:
        #     print("You are healthy.")
        # elif BMI <= 29.9:
        #     print("You are over weight.")
        # elif BMI <= 34.9:
        #     print("You are severely over weight.")
        # elif BMI <= 39.9:
        #     print("You are obese.")
        # else:
        #     print("You are severely obese.")
            
        return redirect('/homepage')
  
def Add_meal(request):
    name = {}
    
    if 'name' in request.GET:
        name = request.GET['name']
    
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(name)


        r = requests.get(api_url, headers={'X-Api-Key': 'pFY/SNtYBMprok0WnT6l1Q==VX5UQavfvBpFrIrU'})
        name = r.json()
    
        # return redirect('/add-meal')
    
    results = name
    context = {
       "calorie": results
    }
    print(results) 
    return render(request, 'mycalorie.html', context)    
 
def nav(request):
    return render(request, 'nav.html')