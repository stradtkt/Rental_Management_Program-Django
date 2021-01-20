from django.db import models
from reviews.models import Review

class RenterManager(models.Manager):
    def validate_renter(self, pd):
        errors = {}
        if len(pd['first_name']) < 2:
            errors['first_name'] = 'Your first name needs to be 2 or more characters'
        elif len(pd['first_name']) > 100:
            errors['first_name'] = 'Your first name needs to be 100 or less characters'

        if len(pd['last_name']) < 2:
            errors['last_name'] = 'Your last name needs to be 2 or more characters'
        elif len(pd['last_name']) > 100:
            errors['last_name'] = 'Your last name needs to be 100 or less characters'
        return errors


class Renter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, unique=True)
    description = models.TextField(default='')
    kids = models.IntegerField(default=0)
    martial_status = models.CharField(max_length=100, default='')
    income = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='photos/renters/%Y/%m/%d/', blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = RenterManager()
    def __str__(self):
        return self.first_name + " " + self.last_name

