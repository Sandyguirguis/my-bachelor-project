from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'subparts', views.SubPartViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
