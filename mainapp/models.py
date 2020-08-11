from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=30)
    short_description = models.CharField(verbose_name='Short description', max_length=100)
    description = models.CharField(verbose_name='Description', max_length=5000)
    img = models.ImageField(verbose_name='Image')
    quantity_of_lectures = models.IntegerField(verbose_name='Quantity of lectures')
