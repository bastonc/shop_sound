from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Customers, Profile

admin.site.register([Customers, Profile])
