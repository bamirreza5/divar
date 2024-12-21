from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Ad
from .Serializer import AdSerializer
from .permissions import IsOwner
from rest_framework import permissions

# Create your views here.
# class show_ad(View):
#     def get(self,request):
#         return HttpResponse("ok")

class AdViewSet(viewsets.ModelViewSet):
    #اگر خواستیم همه رو بگیریم
    # queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)
    def get_permissions(self):

        if self.action in ['list', 'create']:
            return [permissions.IsAuthenticated()]
        return [IsOwner()]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)