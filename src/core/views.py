from django.shortcuts import render
from django.views.generic import TemplateView

from shop.models import Category, Pages, Product

# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        if request.GET.get("search"):
            products = Product.objects.filter(name=str(request.GET["search"]).strip().capitalize())
            context["meta"] = {
                "title": f"Search student {str(request.GET['search'])} | LMS",
                "description": "Search student | LMS",
                "h1": "Search students",
            }
            self.template_name = "students/student_search.html"
        else:
            products = Product.objects.all()
            categories = Category.objects.all()
            page = Pages.objects.filter(name="index")
            if page:
                page_data = page.get()
                context["meta"] = {
                    "title": page_data.seo_title,
                    "description": page_data.seo_description,
                    "h1": page_data.h1,
                }
            else:
                context["meta"] = {
                    "title": "default_title(create index page in static page)",
                    "description": "default_description(create index page in static page)",
                    "h1": "default_h1(create index page in static page)",
                }

            self.template_name = "shop/index.html"
        context["products"] = products
        context["categories"] = categories

        return self.render_to_response(context)
