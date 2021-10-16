from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import Contact, Book


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'title', 'quantity', 'total_quantity', 'details', 'image', 'AdminUpload',
                  'author', 'pages'
                  ]
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        #     'total_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        #     'details': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control'}),
        #     'pages': forms.TextInput(attrs={'class': 'form-control'})
        # }
