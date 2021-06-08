from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .form import ProfileForm
from .models import User
from .models import *
import requests
import bcrypt



def index(request):
    return render(request, 'homepage.html')


# >>>>>> ***************************************** Registrations ********************************

def register(request):
    errors = User.objects.basic_validation(request.POST)
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')    
  
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=hash1)
    # request.session['loginID']= newuser.id
    return redirect("/")


# >>>>>> ***************************************** Login ********************************

def user_login(request):
    userErrors = User.objects.login_validator(request.POST)
    if len(userErrors) > 0:
        for key,val in userErrors.items():
            messages.error(request,val)
        return redirect('/')
    
    user = User.objects.get(email = request.POST['email'])
    request.session['loginID'] = user.id
    return redirect('/user-dashboard')


# >>>>>> ***************************************** User Dashboard ********************************

def Dashboard(request):
    if 'loginID' not in request.session:
        return redirect('/')
 
    if 'loginID' in request.session:
        # user = User.objects.filter(id=request.session['loginID'])
        Foodset= Food.objects.filter(user_id=request.session['loginID']) 
        cnt = Food.objects.filter(user_id=request.session['loginID']).count()  
                
        context = {
                
        'foodset': Foodset,
        'counts' : cnt,
        # 'user' : user
        # 'userlogged': User.objects.get(user_id=request.session['loginID'])
            }
            
        return render(request, 'Dashboard.html', context)
    

# >>>>>> ***************************************** User Profile *************************************

def User_Profile(request):
    if 'loginID' not in request.session:
        return redirect('/')
    context = {
        'userlogged': User.objects.get(id = request.session['loginID'])
    }
    return render(request, 'Profile.html', context)




def add_profile(request):
    if 'loginID' not in request.session:
        return redirect('/')
    
    if request.method == 'POST': 
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        activity = request.POST['activity']       
        ProfileSetting.objects.create(user=User.objects.get(id=request.session['loginID']), age=age , gender=gender, height=height, weight=weight,  activity=activity)
            
        return redirect('/User_Profile')
    
    
# >>>>>> ***************************************** Add Meal from External AIP and save to sqlite *************************************
  
def Add_meal(request):
    
    # if request.method == 'POST':
    #     quantity = request.POST['quantity']
    #     meal = request.POST['meal']
    #     date = request.POST['date']
    if 'loginID' not in request.session:
        return redirect('/')     
    
    
    # user = User.objects.get(id=request.session['user_id'])
    
    all_foods = {}
    
    if 'name' in request.GET:
        
        name = request.GET['name']
        
        url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

        querystring = {"query": name }

        headers = {
            'x-rapidapi-key': "6e9c9a10b3mshed5fde96db16b37p149609jsn35fb89b0ec76",
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
                
       
        data = response.json()
        result = data ['items']
        
        print(result)
        
        for i in result:
            meal_data = Food(name = i['name'],
                             calories = i['calories'],
                             serving_size_g = i['serving_size_g'],
                             fat_total_g = i['fat_total_g'],
                             fat_saturated_g = i['fat_saturated_g'],
                             protein_g = i['protein_g'],
                             sodium_mg = i['sodium_mg'],
                             potassium_mg = i['potassium_mg'],
                             cholesterol_mg = i['cholesterol_mg'],
                             carbohydrates_total_g= i['carbohydrates_total_g'],
                             fiber_g = i['fiber_g'],
                             sugar_g = i['sugar_g'],
                             user=User.objects.get(id=request.session['loginID'])
        
            ) 
            meal_data.save()
      
        all_foods = Food.objects.all().order_by('-id')
        
    context = {
       "items": all_foods
       
    }
    
    
    return render(request, 'mycalorie.html', context)  

# >>>>>> ***************************************** Delete Meal *************************************

def delete(request, id):
    Food.objects.get(id=id).delete()
    return redirect('/')


# >>>>>> ***************************************** Logout *****************************************

def logoutUser(request):
    request.session.clear()
    return redirect("/")