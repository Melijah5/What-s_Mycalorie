from django.db import models
import re , bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validation(self, post_data):
        errors ={}
        if not post_data['firstname'] or not post_data['lastname'] or not post_data['password'] or not post_data['email']:
            errors['fieldes_required'] = 'all fields are required'
            return errors
        if len(post_data ['firstname']) < 2:
            # print('The firstname is less than 2 char!')
            errors['firstname'] = 'First name must be at least 2 char!'
        if len(post_data ['lastname']) < 2:
            # print('The lastname is less than 2 char!')
            errors['lastname'] = 'Last name must be at least 2 char!'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Invalid Email Format'
        emailcheck =self.filter(email=post_data['email'])
        if emailcheck:
            errors['email'] = 'This Email is aleady in use'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be greater than 8 char'
        if post_data['cpassword'] != post_data['password']:
            errors['cpassword'] = 'passwords do not match'
        return errors
    
    
    def login_validator(self, user_data):
        loginErrors = {}
        
        if len(user_data ['email']) < 1:
            # print('The email is less than 1 char!')
            loginErrors['email'] = 'Email Address is required!!'
        getEmail = User.objects.filter(email=user_data['email'])
        print(getEmail)
        if len(getEmail) == 0:
            loginErrors['emailNotexist'] = 'Invalid Email Please register!'
        else:
            user = getEmail[0]
            if not bcrypt.checkpw(user_data['password'].encode(), user.password.encode()):
                loginErrors['password'] = "Incorrect password"
                
        
        return loginErrors

    
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
       
    objects = UserManager()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email}"
    



# >>>> *******************************user Profile ***********************    



class ProfileManager(models.Model):
    def validate_profile(self, profile_text):
        profile_errors = {}
        if not profile_text['age'] or not profile_text['gender'] or not profile_text['height'] or not profile_text['weight'] or not profile_text['activity']:
            profile_errors['fieldes_required'] = 'all fields are required'
            return profile_errors
        
        if int(profile_text['age']) < 1:
            profile_text ['age'] = 'Incorrect age!'
            return profile_errors
        
class ProfileSetting(models.Model):
    user = models.OneToOneField(User, related_name='ProfileSettings', on_delete=models.CASCADE)
    age = models.IntegerField(3, default= 0)
    gender = models.CharField(max_length=10, default=None)
    height = models.FloatField(10, default=0)
    weight = models.FloatField(10, default=0)
    activity = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.age}{self.gender}{self.height}{self.weight}{self.activity}"
    
    objects = ProfileManager()
    
    
# >>>> *******************************  Food ************************* 

class Picture(models.Model):
    file = models.FileField(upload_to='user_images', default='/static/css/image/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name='pictures', on_delete=models.CASCADE)
    profilesetting =models.OneToOneField(ProfileSetting, related_name='pictures', on_delete=models.CASCADE, default=None)

    
    
# >>>> *******************************  Food ************************* 

   
class Food(models.Model):
    
    user = models.ForeignKey(User,related_name='foods', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    calories = models.FloatField(default = 0)
    serving_size_g = models.FloatField(default = 0)
    fat_total_g = models.FloatField(default = 0)
    fat_saturated_g = models.FloatField(default = 0)
    protein_g = models.FloatField(default = 0) 
    sodium_mg = models.FloatField(default = 0)
    potassium_mg = models.FloatField(default = 0)
    cholesterol_mg = models.FloatField(default = 0)
    carbohydrates_total_g = models.FloatField(default = 0)
    fiber_g = models.FloatField(default = 0)
    sugar_g = models.FloatField(default = 0)
    created_at = models.DateTimeField(auto_now=True )
    updated_at = models.DateTimeField(auto_now=True)
    
   
    
    def __str__(self):
        return self.name
    
class BlogManager(models.Manager):
    def validate_blog(self, blog_text):
        errors = {}
        if len(blog_text)<2:
            errors['length'] = 'Blog must be  between 2 - 250 character'
        if len(blog_text)>250: 
            errors['length'] = 'Blog must be  between 2 - 250 character'
        return errors

class Blog(models.Model):
  text = models.CharField(max_length=280)
  user = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)
  
  objects = BlogManager()
  
class Comment(models.Model):
  text = models.CharField(max_length=280)
  user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
  blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)