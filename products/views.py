from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer , CategorySerializer , ProductSerializer
from .models import File , Product , Category
# Create your views here.

#Products Views
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
        serializer = ProductSerializer(product , context={'request':request})
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

#Category Views


class CategoryListView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True , context={'request':request})
        return Response(serializer.data)
    def post(self , request):
        return Response("This method not Allowed" , status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryDetailView(APIView):
    def get(self , request , pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response("Category Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category , context={'request':request})
        return Response(serializer.data)
    def post(self , request , pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response("Category Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request , pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response("Category Not Found", status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileListView(APIView):
    def get(self , request , product_pk):
        files = File.objects.filter(product_id=product_pk)
        serializer = FileSerializer(files, many = True , context={'request':request})
        return Response(serializer.data)
    def post(self , request):
        return Response("This method not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FileDetailView(APIView):
    def get(self , request ,product_pk ,pk):
        try:
            file = File.objects.get(pk=pk , product_id=product_pk )
        except File.DoesNotExist:
            return Response("File Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file , context={'request':request})
        return Response(serializer.data)
    def post(self , request , pk):
        try:
            file = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response("File Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)