from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.shortcuts import redirect


# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, default="Pizza")
    item_desc = models.CharField(max_length=200, default="Pizza awesome")
    item_price = models.IntegerField(default=100)
    item_image = models.CharField(max_length=500,
                                  default='https://image.shutterstock.com/image-photo/cinema-concept-red-striped-boxes-600w-1371235550.jpg')

    def get_absolute_url(self):
        return reverse("FoodApp:detail", kwargs={'pk': self.pk})


class PostContactInfo(models.Model):
    def __str__(self):
        return self.customer_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    customer_name = models.CharField(max_length=200)
    email_id = models.EmailField()
    mobile_no = models.IntegerField()
    message = models.TextField(max_length=700)

    def get_absolute_url(self):
        return reverse('FoodApp:thanks_page')
