from django.db import models


class user(models.Model):
    
    name = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.password


class data(models.Model):
    
    user_name = models.CharField(max_length=20)
    user_path= models.CharField(max_length=50)
    
    category=models.CharField(max_length=20,null=True)
    user_route=models.TextField(null=True)
    user_save=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name


class city_route(models.Model):
    city_name=models.CharField(max_length=20)
    route_name=models.CharField(max_length=100)
    distance=models.CharField(max_length=20)
    path=models.TextField(max_length=500)
    link=models.TextField(max_length=100)
    route_landscape=models.TextField(max_length=100)

class hot_route(models.Model):
    route_name=models.CharField(max_length=100)
    day_consume=models.CharField(max_length=20)
    schedule=models.TextField(max_length=500)
    scenery=models.TextField(max_length=500)

