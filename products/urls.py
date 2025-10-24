from django.urls import path
from .views import ProductListView , ProductsDetailView

urlpatterns = [
    path('products/',ProductListView.as_view() ),
    path('products/<int:pk>/' ,ProductsDetailView.as_view() ),
]