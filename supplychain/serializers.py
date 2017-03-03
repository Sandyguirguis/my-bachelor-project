from rest_framework import serializers
from .models import (Supplier, Product)


class SupplierSerializer(serializers.ModelSerializer):
    """
    A serializer for a Supplier object

    author: Sandy Guirguis
    """

    class Meta:
        model = Supplier
        fields = ('id', 'logo', 'name', 'industry', 'email', 'number', 'phone',
                  'country', 'city', 'address', 'postal_code', 'certificates',
                  'partners', 'facebook',
                  'linkedin')


class ProductSerializer(serializers.ModelSerializer):
    """
    A serializer for a Product object

    author: Sandy Guirguis
    """

    class Meta:
        model = Product
        fields = ('id', 'supplier', 'name', 'description', 'comment')
