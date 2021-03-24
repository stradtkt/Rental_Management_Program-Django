from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from properties.models import Property


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)


class HomePageView(ListView):
    fields = ("photo_main", "price", "bedrooms", "bathrooms")
    model = Property
    context_object_name = "homes"
    template_name = "pages/index.html"


class HomePageDetailsView(DetailView):
    fields = ("owner", "title", "address", "city", "state", "zipcode", "description",
                "price", "bedrooms", "bathrooms", "garage", "sqft", "lot_size", "photo_main",
                "photo_1", "photo_2", "photo_3", "photo_4", "photo_5", "photo_6", "photo_7",
                "photo_8", "photo_9", "photo_10", "photo_11", "photo_12", "list_date", "reviews")
    model = Property
    context_object_name = "home"
    template_name = "pages/details.html"