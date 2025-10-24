from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer , CategorySerializer , ProductSerializer
from .models import File , Product , Category
# Create your views here.

class ProductListView(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)