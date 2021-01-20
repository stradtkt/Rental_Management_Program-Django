from django.db import models


class ReviewManager(models.Manager):
    def validate_review(self, pd):
        errors = {}
        if len(pd['title']) < 2:
            errors['title'] = 'Please make your title 2 or more characters.'
        elif len(pd['title']) > 200:
            errors['title'] = 'Please make your title 200 or less characters.'
        return errors


class Review(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    stars = models.IntegerField(default=5)
    objects = ReviewManager()
    def __str__(self):
        return self.title
