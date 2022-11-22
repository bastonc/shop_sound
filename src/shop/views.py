from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, UpdateView

from accounts.models import Customers, Profile
from core.tasks import (generate_category, generate_product,
                        generate_sub_category)
from shop.basket import Basket
from shop.forms import BasketAddProductForm, OrderCreateForm
from shop.helpers.categories_processing import (get_current_category,
                                                get_current_sub_category,
                                                get_item_product, get_products,
                                                get_sub_category)
from shop.helpers.search_processing import get_header
from shop.models import OrderItem, Product, Order


class CategoryView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/category.html")
        context["current_category"] = get_current_category(category_alias=kwargs["category_name"])
        context["sub_category"] = get_sub_category(category_alias=kwargs["category_name"])
        self.template_name = template_name
        return self.render_to_response(context)


class SubCategoryView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/listing.html")
        if context["products"] is None:
            context["products"] = get_products(sub_category_alias=kwargs["sub_category_name"])
        context["current_sub_category"] = get_current_sub_category(sub_category_alias=kwargs["sub_category_name"])
        context["current_category"] = get_current_category(category_alias=kwargs["category_name"])
        context["form_add_to_basket"] = BasketAddProductForm()
        self.template_name = template_name
        return self.render_to_response(context)


class ProductView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/product.html")
        context["product"] = get_item_product(kwargs["pk_item"])
        context["current_sub_category"] = get_current_sub_category(sub_category_alias=kwargs["sub_category_name"])
        context["current_category"] = get_current_category(category_alias=kwargs["category_name"])
        context["form_add_to_basket"] = BasketAddProductForm()
        self.template_name = template_name
        return self.render_to_response(context)


class BasketView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/basket.html")
        context["basket"] = Basket(self.request)
        context["meta"] = {"title": "Basket | Baston sound shop", "description": "Basket | Baston sound shop"}
        self.template_name = template_name
        return self.render_to_response(context)


class OrderCreateView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/order/create.html")
        form = OrderCreateForm(instance=request.user)
        context["form"] = form
        context["basket"] = Basket(request)
        self.template_name = template_name
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = super().get_context_data()
        form = OrderCreateForm(request.POST)
        basket = Basket(request)
        context, template_name = get_header(request=request, context=context, template_path="shop/order/created.html")
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(
                    user=request.user,
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            basket.clear()
        self.template_name = template_name
        context["order"] = order
        return self.render_to_response(context)


@require_POST
def basket_add(request, pk):
    basket = Basket(request)
    product = get_object_or_404(Product, id=pk)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add_product(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("shop:show_basket")


def basket_remove(request, pk):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=pk)
    basket.remove_product(product)
    return redirect("shop:show_basket")


def generate_category_view(request):
    generate_category.delay()
    return HttpResponse("Category generated")


def generate_sub_category_view(request):
    generate_sub_category.delay()
    return HttpResponse("Sub-category generated")


def generate_product_view(request):
    generate_product.delay()
    return HttpResponse("Products create")
