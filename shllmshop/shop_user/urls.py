from django.urls import path
from .views import UserRegistrationView, UserLoginView

app_name = "shop_user"
urlpatterns = [
    path('create/', UserRegistrationView.as_view(), name="user-registration"),
    path('login/', UserLoginView.as_view(), name="user-login"),
]