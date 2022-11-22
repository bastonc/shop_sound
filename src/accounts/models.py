from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomerManager


class Customers(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First name"), max_length=150, blank=True)
    last_name = models.CharField(_("Last name"), max_length=150, blank=True)
    email = models.EmailField(_("Email address"), unique=True)
    phone = PhoneNumberField(unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    is_content = models.BooleanField(_("content_manager"), default=False, help_text=_("Only for content managers"))
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Buyer")
        verbose_name_plural = _("Buyers")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class Profile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=settings.USER_UPLOAD_IMAGE, null=True, default=settings.DEFAULT_USER_AVATAR)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.email} {self.user.pk}"
