from django.contrib import admin

from lettings.models import LettingReview
from profiles.models import ProfileReview

from .models import Address


admin.site.register(LettingReview)
admin.site.register(Address)
admin.site.register(ProfileReview)
