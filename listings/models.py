from django.db import models
from django.urls import reverse
from datetime import date
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_1 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_2 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_3 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_4 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_5 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    photo_6 = models.ImageField(
        upload_to="photos/listings/%Y/%m/%d/", blank=True, null=True
    )
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(
        verbose_name="Entry Date", default=date.today, blank=True, null=True
    )

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listings:listing-detail", kwargs={"listing_id": self.pk})
