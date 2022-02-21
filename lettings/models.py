from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"
        verbose_name = "Address"

    def __str__(self):
        return f'{self.number} {self.street}'


class AddressReview(Address):
    class Meta:
        proxy = True
        app_label = 'oc_lettings_site'
        verbose_name = Address._meta.verbose_name
        verbose_name_plural = Address._meta.verbose_name_plural


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
