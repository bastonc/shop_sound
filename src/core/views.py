from django.shortcuts import render
from django.views.generic import TemplateView

from shop.models import Category, Pages, Product

from core.helpers.search_processing import get_header

# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/index.html")
        self.template_name = template_name
        return self.render_to_response(context)
