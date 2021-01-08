from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.db import models

#


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
    # Bite_name = models.CharField(max_length=255)
    # Detail_name = models.CharField(max_length=255)
    Depth = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='category ')

    def __str__(self):
        return self.Panel_name + ' | ' + str(self.Site_name)


    def get_absolute_url(self):
        # return reverse('panel_details', args=(str(self.id)))
        return reverse('home')


# Create your models here.


#for N101 양식

class Board_N101(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


#for N102 양식
class Board(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# for N103 양식
class Board_N103(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# for N106 양식
class Board_N106(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# for N109 양식
class Board_N109(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# for T316 양식
class Board_T316(models.Model):
    Site = models.CharField(max_length=10, null=False)
    Operator = models.CharField(max_length=10, null=False)
    Panel_No = models.CharField(max_length=20, null=False)
    Bite = models.CharField(max_length=20, null=False)
    Depth = models.CharField(max_length=20, null=False)
    Geo_Type = models.CharField(max_length=20, null=False)
    Memo = models.CharField(max_length=30, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
