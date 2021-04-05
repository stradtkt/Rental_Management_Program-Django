from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from properties.models import Property
from . import models

def index(request):
    properties = Property.objects.order_by('-address').all()
    context = {
        "properties": properties
    }
    return render(request, 'properties/properties.html', context)



class PropertyDetailsView(DetailView):
    fields = ("owner", "title", "address", "city", "state", "zipcode", "description",
                "price", "bedrooms", "bathrooms", "garage", "sqft", "lot_size", "photo_main",
                "photo_1", "photo_2", "photo_3", "photo_4", "photo_5", "photo_6", "photo_7",
                "photo_8", "photo_9", "photo_10", "photo_11", "photo_12", "list_date", "reviews")
    model = models.Property
    context_object_name = "home"
    template_name = "properties/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyDetailsView, self).get_context_data(*args, **kwargs)
        context['house_featured'] = models.Property.objects.all()
        return context