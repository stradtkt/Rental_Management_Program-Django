from django.db import models
from datetime import datetime
from owners.models import Owner
from reviews.models import Review


class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_2 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_3 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_4 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_5 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_6 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_7 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_8 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_9 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_10 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_11 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    photo_12 = models.ImageField(upload_to='photos/properties/%Y/%m/%d', blank=True, default=None)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
