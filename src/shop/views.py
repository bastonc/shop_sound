from django.http import HttpResponse
from django.views.generic import TemplateView

from shop.helpers.categories_processing import (get_current_category,
                                                get_current_sub_category,
                                                get_products, get_sub_category)
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
        context["products"] = get_products(sub_category_alias=kwargs["sub_category_name"])
        context["current_sub_category"] = get_current_sub_category(sub_category_alias=kwargs["sub_category_name"])
        context["current_category"] = get_current_category(category_alias=kwargs["category_name"])
        self.template_name = template_name
        return self.render_to_response(context)
