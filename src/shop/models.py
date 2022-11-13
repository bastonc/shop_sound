from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseEntity(models.Model):
    index = models.BooleanField(default=True, null=True)
    seo_title = models.CharField(max_length=100, null=True)
    seo_description = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=150, null=True)

    def clean(self):
        super().clean()
        self.name = self.name.lower()
    class Meta:
        abstract = True


class Order(models.Model):
    class STATUS_CHOICE(models.TextChoices):
        NEW = "New", "New"
        APPROVE = "Approve", "Approve"
        DELIVERY = "Delivery", "Delivery"
        CLOSE = "Close", "Close"

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(
        to="shop.Product",
        related_name="products",
        blank=True,
        null=True,
    )
    date_time_create = models.DateTimeField(null=True, auto_now_add=True)
    date_time_update = models.DateTimeField(null=True, auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.NEW, max_length=10)
    order_num = models.UUIDField(unique=True, null=True)

    def total_price(self):
        return sum(product.price for product in self.products.all())

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class Product(BaseEntity):
    class CURRENCY_CHOICES(models.TextChoices):
        UAH = "UAH", "UAH"
        USD = "USD", "USD"

    brand = models.ForeignKey(to="shop.Brand", related_name="brand", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(to="shop.SubCategory", related_name="products", on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, null=True)
    availability = models.BooleanField(default=True, null=True)
    image = models.ImageField(
        upload_to="image/products/", null=True, default=settings.PRODUCT_IMAGE_DEFAULT
    )
    price = models.SmallIntegerField(null=True)
    currency = models.CharField(choices=CURRENCY_CHOICES.choices, default=CURRENCY_CHOICES.UAH, max_length=3)
    url = models.CharField(max_length=100, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.price} "

    def product_price(self):
        return self.price

    def set_url(self):
        category = self.sub_category.category.alias
        sub_category = self.sub_category.alias
        url = f"{category}/{sub_category}/{str(self.name).lower().replace(' ','-').replace('&','-amp-')}"
        alias = f"{str(self.name).lower().replace(' ','-').replace('&','-amp-')}"
        return url, alias

    def save(self, *args, **kwargs):
        self.full_clean()
        self.url, self.alias = self.set_url()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Brand(BaseEntity):
    image = models.ImageField(
        upload_to=settings.PRODUCT_UPLOAD_IMAGE, null=True, default=settings.PRODUCT_IMAGE_DEFAULT
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class SubCategory(BaseEntity):
    category = models.ForeignKey(to="shop.Category", related_name="category", on_delete=models.CASCADE)
    seo_text = models.TextField(max_length=5000, null=True)
    image = models.ImageField(
        upload_to=settings.SUB_CATEGORY_UPLOAD_IMAGE, null=True, default=settings.SUB_CATEGORY_IMAGE_DEFAULT
    )
    alias = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Sub category")
        verbose_name_plural = _("Sub categories")


class Category(BaseEntity):
    seo_text = models.TextField(max_length=5000, null=True)
    image = models.ImageField(
        upload_to=settings.CATEGORY_UPLOAD_IMAGE, null=True, default=settings.CATEGORY_IMAGE_DEFAULT
    )
    alias = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Pages(BaseEntity):
    h1 = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Static page")
        verbose_name_plural = _("Static pages")
