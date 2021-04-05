from django.db import models
from accounts.models import User


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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = OwnerManager()
    def __str__(self):
        return self.name


class ReviewManager(models.Manager):
    def validate_review(self, pd):
        errors = {}
        if len(pd['title']) < 2:
            errors['title'] = 'Please make your title 2 or more characters.'
        elif len(pd['title']) > 200:
            errors['title'] = 'Please make your title 200 or less characters.'
        return errors


class Review(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    stars = models.IntegerField(default=5)
    objects = ReviewManager()
    def __str__(self):
        return self.title