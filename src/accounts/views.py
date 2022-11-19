from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (CreateView, RedirectView, TemplateView,
                                  UpdateView)

from accounts.forms import LoginForm, ProfileForm, RegistrationForm
from accounts.helpers.create_profile import create_profile
from accounts.helpers.token_generator import TokenGenerator
from accounts.models import Profile
from accounts.services.emails import send_registration_email


class Login(LoginView):
    template_name = settings.LOGIN_TEMPLATE
    form_class = LoginForm
    next_page = reverse_lazy("core:index")


class Logout(LogoutView):
    next_page = reverse_lazy("login")


class Registration(CreateView):
    template_name = settings.REGISTRATION_TEMPLATE
    form_class = RegistrationForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        send_registration_email(request=self.request, user_instance=self.object)
        return super().form_valid(form)


class ActivateUser(RedirectView):
    url = reverse_lazy("core:index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, TypeError, ValueError):
            return HttpResponse("Error validation. Incorrect data")
        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()
            login(request, current_user, backend="django.contrib.auth.backends.ModelBackend")
            create_profile(current_user)  # temporary solution
            return super().get(request, *args, **kwargs)

        return HttpResponse("We can't activate you. Incorrect token")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    pk_url_kwarg = "pk"
    form_class = ProfileForm
    template_name = "user/form_update.html"
    meta_page = {
        "title": "Update profile user | LMS",
        "description": "Update profile user | LMS",
        "h1": "Update profile",
    }
    extra_context = {"page": "profile", "meta": meta_page}
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        if request.user.profile.id != kwargs["pk"]:
            return HttpResponse("Wrong! Incorrect profile id")
        return super().get(request, *args, **kwargs)
