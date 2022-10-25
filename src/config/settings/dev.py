from config.settings.base import *  # noqa

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default_sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
        "TEST": {"NAME": "test"},
    },
}

STATIC_URL = "static/"
MEDIA_URL = "media/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), os.path.join(BASE_DIR, "media")]

# Product image
PRODUCT_UPLOAD_IMAGE = "static/image/products/"
PRODUCT_IMAGE_DEFAULT = os.path.join(STATIC_URL, "image/products/non-image.png")

# Sub-category image
SUB_CATEGORY_UPLOAD_IMAGE = os.path.join(STATIC_URL, "image/sub-category/")
SUB_CATEGORY_IMAGE_DEFAULT = os.path.join(STATIC_URL, "image/sub-category/non-image.png")

# Category image
CATEGORY_UPLOAD_IMAGE = os.path.join(STATIC_URL, "image/category/")
CATEGORY_IMAGE_DEFAULT = os.path.join(STATIC_URL, "image/category/non-image.png")