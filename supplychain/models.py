from __future__ import unicode_literals
from django.db import models


class Supplier(models.Model):
    """
    Represents a single supplier
    Author: Sandy Guirguis
    """
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('beverages', 'Beverages'),
        ('steel', 'Steel'),
        ('automotive', 'Automotive'),
        ('electronics', 'Electronics')
    )
    logo = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=256, unique=True)
    industry = models.CharField(max_length=256, choices=CATEGORY_CHOICES)
    email = models.EmailField()
    number = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=256)
    certificates = models.CharField(max_length=256, null=True, blank=True)
    partners = models.CharField(max_length=256, null=True, blank=True)
    facebook = models.CharField(max_length=256, null=True, blank=True)
    linkedin = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name + " working in the " + self.industry + " industry"


class Product(models.Model):
    '''
    Represents a single product
    Author: Sandy Guirguis
    '''
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return self.name + " supplied by: " + self.supplier.name


class Part(models.Model):
    """
    Represents a single part of a product
    Author: Sandy Guirguis
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='part', null=True)
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=500, null=True)
    comment = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name + " is a part of product" + self.product.name
