from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class show_ad(View):
    def get(self,request):
        return HttpResponse("ok")