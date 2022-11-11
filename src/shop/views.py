from django.http import HttpResponse
from django.views.generic import TemplateView

from core.tasks import generate_category, generate_sub_category, generate_product
from shop.helpers.categories_processing import (get_current_category,
                                                get_current_sub_category,
                                                get_products,
                                                get_sub_category,
                                                get_item_product)
from shop.helpers.search_processing import get_header


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
        self.template_name = template_name
        return self.render_to_response(context)


class ProductView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/product.html")
        context["product"] = get_item_product(kwargs['pk_item'])
        context["current_sub_category"] = get_current_sub_category(sub_category_alias=kwargs["sub_category_name"])
        context["current_category"] = get_current_category(category_alias=kwargs["category_name"])
        self.template_name = template_name
        return self.render_to_response(context)


def generate_category_view(request):
    generate_category.delay()
    return HttpResponse("Category generated")


def generate_sub_category_view(request):
    generate_sub_category.delay()
    return HttpResponse("Sub-category generated")


def generate_product_view(request):
    generate_product.delay()
    return HttpResponse("Products create")
