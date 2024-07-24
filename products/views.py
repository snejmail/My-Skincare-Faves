from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
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
        return user.favorite_products.all()


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
    pass


def review_product(request, pk):
    pass

