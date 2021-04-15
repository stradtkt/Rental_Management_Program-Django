from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from properties.models import Property
from owners.models import Owner


def dashboard(request):
    labels_homes = []
    data_homes = []
    queryset_homes = Property.objects.all()
    for home in queryset_homes:
        labels_homes.append(home.id)
        data_homes.append(home.price)
    homes = Property.objects.all()[:3]
    context = {
        "labels": labels_homes,
        "data": data_homes,
        "homes": homes
    }
    return render(request, "dashboard/index.html", context)
