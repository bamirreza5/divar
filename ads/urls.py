from django.urls import path,include
from .views import show_ad

urlpatterns = [
    path('my_ad/', show_ad.as_view() , name='show_ad'),
]