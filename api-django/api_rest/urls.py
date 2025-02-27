from django.urls import path
from .views.users import RegisterUserView
from .views.auth import Login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path("login/", Login, name="login"),
    
]
