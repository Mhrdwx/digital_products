from rest_framework import serializers
from .models import Product , File , Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("id",'title' , 'description' , 'avatar' , "url")


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ("id",'title' , 'file' , "url")

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many = True)
    files = FileSerializer(many = True)
    class Meta:
        model = Product
        fields = ('id' , 'title' , 'description' , "avatar" , "categories" , "files" , "url")


