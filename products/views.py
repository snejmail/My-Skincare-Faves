from django.contrib.auth.decorators import login_required
from django.db import models
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Product, Like, Review
from .forms import ProductForm, ReviewForm


class CatalogueView(LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'catalogue.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_products.all()

        sort_by = self.request.GET.get('sort_by', 'name')
        if sort_by == 'price':
            queryset = queryset.order_by('price')
        elif sort_by == 'type':
            queryset = queryset.order_by('product_type')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Annotate like counts for user and other users' products
        user_products = user.favorite_products.all().annotate(like_count=models.Count('likes'))
        other_users_products = Product.objects.exclude(id__in=user.favorite_products.values_list('id', flat=True))
        other_users_products = other_users_products.annotate(like_count=models.Count('likes'))

        # Create a map for like counts of other users' products
        like_count_map = {product.name.lower(): product.like_count for product in other_users_products}

        # Update user products with the like count from the other users' products map
        for product in user_products:
            product_name = product.name.lower()
            # Fetch like count from the map if it exists
            product.like_count = like_count_map.get(product_name, 0)

        # Add context data
        context["liked_products"] = user.likes.values_list('product_id', flat=True)
        context["other_users_products"] = other_users_products
        context["user_products"] = user_products

        return context


class ProductCreateView(LoginRequiredMixin, views.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.user.favorite_products.add(self.object)
        return response


class ProductDetailView(LoginRequiredMixin, views.DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        context['user_has_liked'] = product.likes.filter(user=user).exists()
        return context


class ProductUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'
    success_url = reverse_lazy('catalogue')


class ProductDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('catalogue')


@login_required
def like_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, product=product)
    if not created:
        like.delete()

    return redirect('catalogue')


def review_product(request, pk):
    pass

