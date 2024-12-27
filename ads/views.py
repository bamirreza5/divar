from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Ad
from .Serializer import AdSerializer,CategorySerializer, CitySerializer
from .permissions import IsOwner
from rest_framework import permissions
from ads.models import Category, City

# Create your views here.
# class show_ad(View):
#     def get(self,request):
#         return HttpResponse("ok")

class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [permissions.IsAuthenticated()]
        return [IsOwner()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        city_id = self.request.query_params.get('city', None)
        if city_id:
            return Category.objects.filter(city_id=city_id)
        return Category.objects.all()

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
