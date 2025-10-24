from django.urls import path
from .views import ProductListView, ProductsDetailView, CategoryDetailView, CategoryListView, FileDetailView, \
    FileListView

urlpatterns = [
    path('products/',ProductListView.as_view() , name='product-list' ),
    path('products/<int:pk>/' ,ProductsDetailView.as_view() , name='product-detail' ),
    path('categories/',CategoryListView.as_view() , name='category-list' ),
    path('categories/<int:pk>/' ,CategoryDetailView.as_view() , name='category-detail' ),
    path('files/',FileListView.as_view() , name='file-list' ),
    path('files/<int:pk>/' ,FileDetailView.as_view() , name='file-detail' ),
]