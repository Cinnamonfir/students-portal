from django import forms
from django.forms import ModelForm
from .models import Student

class Studentform(ModelForm):
        class Meta:
            model = Student
            fields = '__all__'
        


