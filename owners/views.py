from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from properties.models import Property


class OwnerListView(ListView):
    fields = ("name", "email", "photo", "description", "phone", "reviews")
    model = models.Owner
    context_object_name = "owners"
    template_name = "owners/owners.html"


class OwnerDetailView(DetailView):
    model = models.Owner
    context_object_name = "owner"
    template_name = "owners/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OwnerDetailView, self).get_context_data(*args, **kwargs)
        context['properties'] = Property.objects.filter(owner=context)
        return context