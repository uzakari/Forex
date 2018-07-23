from django.forms import ModelForm, TextInput, Textarea, Select, PasswordInput,EmailField
from .models import City, Comment, Register


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'city name'})}


class BlogPostForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
                   'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Post '})}


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['First_name', 'Last_name', 'email', 'gender', 'city',  'password']
        widgets = {'First_name': TextInput(attrs={'class': 'form-control'}),
                   'Last_name':   TextInput(attrs={'class': 'form-control'}),
                   'email':  TextInput(attrs={'class': 'form-control'}),
                   'gender': Select(attrs={'class': 'form-check-input,col-md-6, form-check-inline, form-check-label'}),
                   'password': TextInput(attrs={'class': 'form-control'})}


