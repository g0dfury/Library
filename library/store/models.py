from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, null = False)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=25, null = False)
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
