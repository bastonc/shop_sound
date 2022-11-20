from accounts.models import Profile


def create_profile(user):
    Profile.objects.create(user=user)
