from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from ecom.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
