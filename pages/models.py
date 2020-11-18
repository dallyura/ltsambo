from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name =  models.CharField(max_length=255)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # return reverse('panel_details', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    Site_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Panel_name = models.CharField(max_length=255)
    Operator_name = models.CharField(max_length=255)
    Bite_name = models.CharField(max_length=255)
    Detail_name = models.CharField(max_length=255)
    Depth = models.CharField(max_length=255)
    # post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='category ')

    def __str__(self):
        return self.Panel_name + ' | ' + str(self.Site_name)


    def get_absolute_url(self):
        # return reverse('panel_details', args=(str(self.id)))
        return reverse('home')
