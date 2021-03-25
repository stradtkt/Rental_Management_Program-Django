from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


def dashboard(request):
    context = {}
    return render(request, "dashboard/index.html", context)
