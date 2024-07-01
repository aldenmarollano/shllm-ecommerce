# from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import ShopUserForm
from .models import ShopUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

class UserRegistrationView(View):
    def get(self, request):
        form = ShopUserForm()
        context = {
            'form':form
        }
        return render(request, 'user_registration.html', context)

    def post(self, request):
        form = ShopUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return render(request, 'user_registration.html', {'form': form})

        return redirect('../create/')
    

    
    
class UserLoginView(View):

    def get(self, request):
        context = {
            'form': {},
            'errors': []
        }
        return render(request, 'user_login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return HttpResponse("Home Page")
        
        else:
            try:
                user = ShopUser.objects.get(username=username)
                messages.error(request, "Invalid password.")
                
            except ShopUser.DoesNotExist:
                messages.error(request, "Invalid username.")
        
        context = {
            'errors': messages.get_messages(request)
        }

        return render(request, 'user_login.html', context)
    
def logout_view(request):
    logout(request)
    