# from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from .forms import ShopUserForm
from .models import ShopUser

# Create your views here.

class UserRegistration(View):
    def get(self, request):
        form = ShopUserForm()
        context = {
            'form':form
        }
        return render(request, 'user_registration.html', context)

    def post(self, request):
        form = ShopUserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data['user_password'])
            form.save()
        else:
            print(form.errors)
            return render(request, 'user_registration.html', {'form': form})

        return redirect('../create/')
    

    
    
class UserLogin(View):

    def get(self, request):
        form = ShopUserForm()
        context = {
            'forms': form
        }
        return render(request, 'user_login.html', context)

    def post(self, request, username, password):
        username = request.POST.get('username')
        password = request.POST.get('password')

        form = ShopUserForm.objects.get(username = username, user_password = password)

        pass

    