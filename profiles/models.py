from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"
        verbose_name = "Profile"

    def __str__(self):
        return self.user.username


class ProfileReview(Profile):
    class Meta:
        proxy = True
        app_label = 'oc_lettings_site'
        verbose_name = Profile._meta.verbose_name
        verbose_name_plural = Profile._meta.verbose_name_plural
