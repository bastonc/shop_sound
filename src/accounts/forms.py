from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from accounts.models import Profile
from accounts.validators import validate_phone_email


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "phone", "email", "password1", "password2")


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "birth_date", "city")


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_("Email or phone number"), widget=TextInput(attrs={"autofocus": True}),
                             validators=[validate_phone_email])
