from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.city.name})"

    
class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', default='default_image.jpg',blank=False)   
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    contact_number = PhoneNumberField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title