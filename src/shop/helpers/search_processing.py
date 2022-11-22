from shop.models import Category, Pages, Product, SubCategory


def get_meta_data_page(page_name):
    page = Pages.objects.filter(name=page_name)
    if page:
        page_data = page.get()
        meta_data = {
            "title": page_data.seo_title,
            "description": page_data.seo_description,
            "h1": page_data.h1,
        }
    else:
        meta_data = {
            "title": "default_title(create index page in static page)",
            "description": "default_description(create index page in static page)",
            "h1": "default_h1(create index page in static page)",
        }
    return meta_data


def get_header(request, context, template_path):
    categories = Category.objects.all()
    if request.GET.get("search"):
        print("request search:", request.GET["search"].strip().lower())
        context["products"] = Product.objects.filter(name__icontains=str(request.GET["search"]).strip())
        print("Found products:", context["products"])
        context["meta"] = get_meta_data_page(page_name="search")
        template_name = "shop/search.html"
    else:
        context["products"] = None
        context["meta"] = get_meta_data_page(page_name="index")
        template_name = template_path

    # context["sub_category"] = sub_categories TODO add output sub categories in main menu
    # context["products"] = products TODO get top products
    context["categories"] = categories
    return context, template_name
