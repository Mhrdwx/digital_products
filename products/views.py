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
        serializer = ProductSerializer(products, many=True , context={'request':request})
        return Response(serializer.data)
    def post(self , request):
        return Response({'message':"This method not Allowed"} , status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ProductsDetailView(APIView):
    def get(self,request , pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def post(self , request , pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request , pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product Not Found", status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

