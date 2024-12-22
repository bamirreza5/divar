from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/' , auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login/'), name='logout'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    # path('token/', 
    #     jwt_views.TokenObtainPairView.as_view(), 
    #     name ='token_obtain_pair'),
    # path('token/refresh/', 
    #     jwt_views.TokenRefreshView.as_view(), 
    #     name ='token_refresh')
]