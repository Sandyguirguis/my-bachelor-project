from rest_framework import viewsets
from .models import (Supplier, Product, Part)
from .serializers import (
    SupplierSerializer, ProductSerializer,
    PartSerializer)
# from rest_framework_xml.parsers import XMLParser
# from rest_framework_xml.renderers import XMLRenderer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a list of suppliers

    author: Sandy Guirguis
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # parser_classes = (XMLParser,)
    # renderer_classes = (XMLRenderer,)


class PartViewSet (viewsets.ModelViewSet):
    """
    This viewset automatically provides a list of parts

    author: Sandy Guirguis
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset provides a list of products with their parts

    Author: Sandy Guirguis
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
