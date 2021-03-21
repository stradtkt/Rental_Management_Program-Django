from django.db import models
from reviews.models import Review

class OwnerManager(models.Manager):
    def validate_owner(self, pd):
        errors = {}
        if len(pd['name']) < 2:
            errors['name'] = 'Your name needs to be 2 or more characters.'
        elif len(pd['name']) > 100:
            errors['name'] = 'Your name cannot be more than 100 characters.'

        if len(pd['email']) > 150:
            errors['email'] = 'Your name cannot be more than 150 characters.'
        return errors


class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, unique=True)
    photo = models.ImageField(upload_to='photos/owners/%Y/%m/%d/', blank=True)
    description = models.TextField(default='')
    phone = models.CharField(max_length=100)
    reviews = models.ForeignKey(Review, on_delete=models.DO_NOTHING, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = OwnerManager()
    def __str__(self):
        return self.name