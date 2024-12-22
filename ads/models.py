from django.db import models

from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', default='default_image.jpg')   
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    contact_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title