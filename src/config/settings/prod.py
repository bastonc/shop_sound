from config.settings.base import *  # noqa

CURRENT_ENV = "PROD"
print(CURRENT_ENV)

DEBUG = False

ALLOWED_HOSTS = ["localhost"]

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
    },
}

STATIC_ROOT = "static_collect/"
STATIC_URL = "static/"

MEDIA_ROOT = "media_collect/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/"), os.path.join(BASE_DIR, "media")]

# Product image
PRODUCT_UPLOAD_IMAGE = "/image/products/"
PRODUCT_IMAGE_DEFAULT = "image/non-image.png"

# Sub-category image
SUB_CATEGORY_UPLOAD_IMAGE = "/image/sub-category/"
SUB_CATEGORY_IMAGE_DEFAULT = "image/non-image.png"

# Category image
CATEGORY_UPLOAD_IMAGE = "/image/category/"
CATEGORY_IMAGE_DEFAULT = "image/non-image.png"
