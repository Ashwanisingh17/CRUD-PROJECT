from socket import fromshare
from django import forms
from django.core import validators
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
          
        }