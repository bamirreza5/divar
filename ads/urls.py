from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet ,  basename='ad')

urlpatterns = [
    path('api/', include(router.urls)),
]