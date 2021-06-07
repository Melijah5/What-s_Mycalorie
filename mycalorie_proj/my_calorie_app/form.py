from django import forms
from django.contrib.auth.models import *
from .models import ProfileSetting

# from .models import Image


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('image',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileSetting
        fields = '__all__'