from django.db import models
from datetime import datetime

class Product(models.Model):

    x= [
        ('phone', 'phone'),
        ('computer', 'computer'),
    ]

    name= models.CharField(max_length=100, default='Product Name')
    content= models.TextField(null=True, blank=True, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='photo', default= 'photos/26/08/09/9.png')
    condition = models.BooleanField(default=True)
    category= models.CharField(max_length=50, null=True, blank=True, choices=x)

    def __str__(self):

        return self.name

    # class Meta:
        
    #     verbose_name = 'product'
    #     ordering = ['name']

class Test(models.Model):

    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)
