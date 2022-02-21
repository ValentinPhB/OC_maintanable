from django.contrib import admin

from lettings.models import LettingReview, AddressReview
from profiles.models import ProfileReview


admin.site.register(LettingReview)
admin.site.register(AddressReview)
admin.site.register(ProfileReview)
