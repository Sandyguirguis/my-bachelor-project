from rest_framework import serializers
from .models import (Supplier, Product, Part, SubPart)


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
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


class SubPartSerializer(serializers.HyperlinkedModelSerializer):
    """
    A serializer for a Subpart object

    Author: Sandy Guirguis
    """
    class Meta:
        model = SubPart
        fields = ('id', 'part', 'name', 'description', 'comment')


class PartSerializer(serializers.HyperlinkedModelSerializer):
    """
    A serializer for a Part in a Product

    author: Sandy Guirguis
    """
    subpart = SubPartSerializer(many=True)

    class Meta:
        model = Part
        fields = ('id', 'product', 'name', 'description', 'comment', 'subpart')

    def create(self, validated_data):
        subparts_data = validated_data.pop('subpart')
        part = Part.objects.create(**validated_data)
        for subparts_data in subparts_data:
            SubPart.objects.create(part=part, **subparts_data)
        return part

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.comment = validated_data.get(
            'comment', instance.comment)
        instance.part = validated_data.get(
            'part', instance.part)
        return instance


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    A serializer for a Product object

    author: Sandy Guirguis
    """

    part = PartSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'supplier', 'name', 'description', 'comment', 'part')

    def create(self, validated_data):
        parts_data = validated_data.pop('part')
        product = Product.objects.create(**validated_data)
        for parts_data in parts_data:
            Part.objects.create(product=product, **parts_data)
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.comment = validated_data.get(
            'comment', instance.comment)
        instance.part = validated_data.get(
            'part', instance.part)
        return instance
