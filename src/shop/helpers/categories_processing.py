from shop.models import Category, Pages, Product, SubCategory


def get_sub_category(category_alias):
    category = Category.objects.filter(alias=category_alias).get()
    sub_categories = SubCategory.objects.filter(category=category)
    return sub_categories


def get_products(sub_category_alias):
    sub_category = SubCategory.objects.filter(alias=sub_category_alias).get()
    products = Product.objects.filter(sub_category=sub_category.id)
    return products


def get_current_category(category_alias):
    category = Category.objects.filter(alias=category_alias).get()
    return category


def get_current_sub_category(sub_category_alias):
    sub_category = SubCategory.objects.filter(alias=sub_category_alias).get()
    return sub_category


def get_item_product(id_product):
    product_item = Product.objects.get(pk=id_product)
    return product_item


def get_top_product():
    top_products = Product.objects.filter(top_item=True)
    return top_products
