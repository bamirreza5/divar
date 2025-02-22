from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .views import LoginWithOTP, ValidateOTP

urlpatterns = [
    path('login/' , auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login/'), name='logout'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    # path('token/', 
    #     jwt_views.TokenObtainPairView.as_view(), 
    #     name ='token_obtain_pair'),
    # path('token/refresh/', 
    #     jwt_views.TokenRefreshView.as_view(), 
    #     name ='token_refresh'),
    path('login-with-otp/', LoginWithOTP.as_view(), name='login-with-otp'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
]