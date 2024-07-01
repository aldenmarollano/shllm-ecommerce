from django.urls import path
from .views import UserRegistration, UserLogin

app_name = "shop_user"
urlpatterns = [
    path('create/', UserRegistration.as_view(), name="user-registration"),
    path('login/', UserLogin.as_view(), name="user-login"),
]