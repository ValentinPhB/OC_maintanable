from django.db import models
from oc_lettings_site.models import Address


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='Letting')

    class Meta:
        verbose_name_plural = "Lettings"
        verbose_name = "Letting"

    def __str__(self):
        return self.title


class LettingReview(Letting):
    class Meta:
        proxy = True
        app_label = 'oc_lettings_site'
        verbose_name = Letting._meta.verbose_name
        verbose_name_plural = Letting._meta.verbose_name_plural
