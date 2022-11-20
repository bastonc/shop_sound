import random

from celery import shared_task
from django.conf import settings
from faker import Faker

from shop.models import Brand, Category, Product, SubCategory


@shared_task
def generate_category():
    categories_name = ["Mixing consoles", "Microphones", "ADC-DAC", "Processors", "Compressors", "Equalizers"]
    category_obj_list = []
    for category in categories_name:
        param = {
            "index": True,
            "name": category,
            "seo_title": f"{category} - by Best price | Baston Sound Shop",
            "seo_description": f"{category} - by Best price | Baston Sound Shop",
            "alias": str(category).lower().replace(" ", "-"),
            "image": settings.CATEGORY_IMAGE_DEFAULT,
        }
        category_obj_list.append(Category(**param))
    Category.objects.bulk_create(category_obj_list)


@shared_task
def generate_sub_category():
    sub_categories = {
        "mixing-consoles": ["Analogue consoles", "Digital consoles", "Consoles with Amp"],
        "microphones": ["Condenser microphones", "Dynamic microphones", "Instrumental microphones"],
        "adc-dac": ["Sound interfaces", "Sound card"],
        "processors": ["Reverb", "Pitch-tone", "Multiprocessing", "Delay"],
        "compressors": ["Multiband", "Analog compressor", "Digital compressor"],
        "equalizers": ["Parametric", "Graphic", "Paragraphic"],
    }
    sub_category_obj_list = []
    for category, sub_categories_list in sub_categories.items():
        current_category = Category.objects.filter(alias=category).get()
        for sub_category in sub_categories_list:
            param = {
                "index": True,
                "name": sub_category,
                "seo_title": f"{sub_category} - by Best price | Baston Sound Shop",
                "seo_description": f"{sub_category} - by Best price | Baston Sound Shop",
                "alias": str(sub_category).lower().replace(" ", "-"),
                "category": current_category,
                "image": settings.SUB_CATEGORY_IMAGE_DEFAULT,
            }
            sub_category_obj_list.append(SubCategory(**param))
    SubCategory.objects.bulk_create(sub_category_obj_list)


@shared_task
def generate_product():
    fake = Faker(locale="en")
    brands_list = ["Allen&Heath", "Soundcraft", "Drawmer", "Klark-Tekhnik", "RME"]
    brand_obj_list = []
    for brand in brands_list:
        param = {
            "index": True,
            "image": settings.PRODUCT_IMAGE_DEFAULT,
            "name": brand,
            "seo_title": f"{brand} in Baston Sound Shop",
            "seo_description": f"{brand} in Baston Sound Shop",
        }
        brand_obj_list.append(Brand(**param))
    Brand.objects.bulk_create(brand_obj_list)
    sub_categories = SubCategory.objects.all()
    brands = Brand.objects.all()
    product_obj_list = []
    for sub_category in sub_categories:
        for _ in range(5):
            brand = brands[random.randint(0, 4)]
            product_name = f"{brand.name} {fake.word(ext_word_list=['KRK5', 'Square one', 'DL-241', 'GL-3200'])}"
            param = {
                "brand": brand,
                "name": product_name,
                "seo_title": f"{product_name} - by Best price | Baston Sound Shop",
                "seo_description": f"{product_name} - by Best price | Baston Sound Shop",
                "sub_category": sub_category,
                "description": fake.sentence(nb_words=10),
                "availability": True,
                "image": settings.PRODUCT_IMAGE_DEFAULT,
                "price": 10000,
                "currency": "UAH",
            }
            # product_obj_list.append(Product(**param))
            product = Product(**param)
            product.save()
    # Product.objects.bulk_create(product_obj_list)
