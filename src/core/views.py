from django.views.generic import TemplateView

from shop.forms import BasketAddProductForm
from shop.helpers.categories_processing import get_top_product
from shop.helpers.search_processing import get_header


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context, template_name = get_header(request=request, context=context, template_path="shop/index.html")
        context["top_products"] = get_top_product()
        self.template_name = template_name
        return self.render_to_response(context)
