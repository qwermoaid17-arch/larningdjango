from django.db import models

class Female(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name
    

    
class Male(models.Model):

    name = models.CharField(max_length=50)

    girls = models.OneToOneField(Female, on_delete=models.CASCADE, )

    def __str__(self):

        return self.name

    
class Product(models.Model):

    name_products = models.CharField(max_length=50)

    def __str__(self):

        return self.name_products
    
class User(models.Model):

    name = models.CharField(max_length=50)

    prod = models.ForeignKey(Product, max_length=50, on_delete=models.CASCADE)

    def __str__(self):

        return self.name

class Videw(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):

        return self.title
    
class username(models.Model):

    name = models.CharField(max_length=50)

    vid = models.ManyToManyField(Videw, max_length=50,)

    def __str__(self):

        return self.name




