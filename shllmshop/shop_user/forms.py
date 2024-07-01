from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ShopUser

class ShopUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ShopUser
        fields = ('first_name', 'last_name','password1', 'password2', 'username', 'email', 'birth_date')
