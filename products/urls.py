from django.urls import path, include
from .views import (
    CatalogueView, ProductCreateView, ProductDetailView,
    ProductUpdateView, ProductDeleteView, like_product, review_product
)

urlpatterns = (
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('<int:pk>/like/', like_product, name='like_product'),
    path('<int:pk>/review/', review_product, name='review_product'),
)