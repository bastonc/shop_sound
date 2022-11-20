from config.settings.base import *  # noqa

CURRENT_ENV = "DEV"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default_postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "github_actions",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
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
