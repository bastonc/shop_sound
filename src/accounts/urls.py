from django.urls import path

from accounts.views import Login, Logout, Registration, RegisterConfirmThankYou, ActivateUser, ProfileView, \
    EditProfileView, RegistrationComplete, HistoryOrderUser

app_name = "accounts"
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registration/", Registration.as_view(), name="registration"),
    path("registration-confirm", RegisterConfirmThankYou.as_view(), name="register_confirm_thankyou"),
    path("activate/<str:uuid64>/<str:token>", ActivateUser.as_view(), name="activate_user"),
    path("registration-complete", RegistrationComplete.as_view(), name="registration_complete"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("edit-profile/<int:pk>", EditProfileView.as_view(), name="edit_profile"),
    path("order-history/<int:pk>", HistoryOrderUser.as_view(), name="orders_history_user"),
]
