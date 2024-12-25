from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class City(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', default='default_image.jpg',blank=False)   
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    contact_number = PhoneNumberField()
    category = models.CharField(max_length=255, default='default_category')
    city = models.CharField(max_length=10 , default='default_city')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title