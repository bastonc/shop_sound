from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from shop.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class BasketAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]

    def clean_postal_code(self):
        postal_code = self.cleaned_data["postal_code"]
        if len(str(postal_code)) > 6:
            raise ValidationError("Only 5 digits")
        return postal_code

