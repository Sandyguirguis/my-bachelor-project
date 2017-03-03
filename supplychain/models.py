from __future__ import unicode_literals
from django.db import models
#from data_importer.importers import XMLImporter


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
    name = models.CharField(max_length=256)
    industry = models.CharField(max_length=256, choices=CATEGORY_CHOICES)
    email = models.CharField(max_length=256)
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
        return self.name


# class MyXMLImporterModel(XMLImporter):
#     root = 'supplychain.xml'

#     class Meta:
#         model = Supplier


class Product(models.Model):
    '''
    Representas a single product
    Author: Sandy Guirguis
    '''
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    comment = models.CharField(max_length=256)
