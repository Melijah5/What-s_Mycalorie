from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# from .models import User
from .models import *
import requests
import bcrypt
from django.db.models import Sum



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
        cnt = + Food.objects.filter(user_id=request.session['loginID']).count()
        mycalorie = Foodset.aggregate(sum_calorie=Sum('calories'))
        if mycalorie['sum_calorie'] is None:
            totalcalorie = mycalorie['sum_calorie'] 
            calorieLeft = 0
            performances = 0
        else:
            totalcalorie = round(mycalorie['sum_calorie'] ) 
            calorieLeft = round(2000 - totalcalorie)
            performances = round((totalcalorie/2000) * 100)
        
        context = {
                
        'foodset': Foodset,
        'counts' : cnt,
        'totalcalorie' : totalcalorie,
        'calorieLeft' : calorieLeft,
        'performances' : performances,
        # 'user' : user
        'userlogged': User.objects.get(id=request.session['loginID'])
            }
            
        return render(request, 'Dashboard.html', context)
    

# >>>>>> ***************************************** User Profile *************************************

def User_Profile(request):
    
    images = Picture.objects.all()

    context = {
        'images': images,
        'userlogged': User.objects.get(id = request.session['loginID'])
    }
    return render(request, 'Profile.html', context)

def add_profile(request):
       
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        activity = request.POST['activity']
        # profile_id = request.POST['profile_id']
        user = User.objects.get(id = request.session['loginID'])
        # profilesetting =ProfileSetting.objects.get(id = profile_id)
        new_profile = ProfileSetting.objects.create(user=user, age=age , gender=gender, height=height, weight=weight,  activity=activity)
        new_file= Picture(file=request.FILES['image'], profilesetting=new_profile, user=user)   
        new_file.save()
            
    return redirect('/add-profile')
    
    
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
    return redirect(f'/user-dashboard')

# >>>>>> ***************************************** blog *****************************************

def blog(request):
    if 'loginID' not in request.session:
        return redirect('/')
    # context = {
    #     'userlogged': User.objects.get(id = request.session['loginID'])
    # }
    if 'loginID' in request.session:
        blogs = Blog.objects.all().order_by('-id')
        comments = Comment.objects.all().order_by('-id')
        user = User.objects.get(id= request.session['loginID'])
        context = {
            'blogs':blogs,
            'comments': comments,
            'user': user
        }
    
    
    return render(request, 'blog.html', context)



# >>>>>> ***************************************** add_blog *****************************************
def add_blog(request):
    blog_text = request.POST['blog_text']
    errors = Blog.objects.validate_blog(blog_text)
    if len(errors)> 0:
        for key, val in errors.items():
            messages.errors(request,val)
        return redirect('/blog')
    user = User.objects.get(id = request.session['loginID'])
    Blog.objects.create(text=blog_text, user=user)
    
    all_blogs = Blog.objects.all()
    context = {
        "all_blogs":all_blogs
    }
    return render(request, 'blog.html', context)


# >>>>>> ***************************************** edit_blog *****************************************
def edit_blog(request, blog_id):
    blog_to_edit = Blog.objects.get(id=blog_id)
    context = {
        "blog" : blog_to_edit
    }
    return render(request, 'edit-blog.html', context)


# >>>>>> ***************************************** modify_blog *****************************************
def modify_blog(request):
    if request.method == 'POST':
        blog_id = request.POST['blog_id']
        new_blog = request.POST['blog_text']
        blog_to_edit = Blog.objects.get(id=blog_id)
        blog_to_edit.text - new_blog
        blog_to_edit.save()
        return redirect('/blog')

# >>>>>> ***************************************** add_comment *****************************************
def add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST['comment_text']
        blog_id = request.POST['blog_id']
        user = User.objects.get(id = request.session['loginID'])
        blog = Blog.objects.get(id=blog_id)
        Comment.objects.create(text=comment_text, user=user , blog=blog)
   
        return redirect(f'/blog')



# >>>>>> ***************************************** delete_blog *****************************************

def delete_blog(request, blog_id):
    myblog= Blog.objects.get(id=blog_id)
    myblog.delete()
    return redirect('/add-blog')


# >>>>>> ***************************************** Logout *****************************************

def logoutUser(request):
    request.session.clear()
    messages.info(request, "You have successfully logged out.")
    return redirect("/")