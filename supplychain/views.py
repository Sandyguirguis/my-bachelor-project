from rest_framework import viewsets
from .models import (Supplier, Product)
from .serializers import (
    SupplierSerializer, ProductSerializer)
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a list of suppliers

    author: Sandy Guirguis
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #parser_classes = (XMLParser,)
    #renderer_classes = (XMLRenderer,)


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a list of products

    author: Sandy Guirguis
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
