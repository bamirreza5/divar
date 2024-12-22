from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ads import models
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def dashboard(request):
    # ads = models.Ad.objects.all()
    ads = models.Ad.objects.filter(user = request.user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'ads': ads})
