from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CategoryViewSet, CityViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'cities', CityViewSet, basename='city')

urlpatterns = [
    path('api/', include(router.urls)),
]
