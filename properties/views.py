from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
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


def add_property(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        owner = User.objects.get(id=user_id)
        title = request.POST['title']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        description = request.POST['description']
        price = request.POST['price']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        garage = request.POST['garage']
        sqft = request.POST['sqft']
        lot_size = request.POST['lot_size']
        photo_main = request.POST['photo_main']
        photo_1 = request.POST['photo_1']
        photo_2 = request.POST['photo_2']
        photo_3 = request.POST['photo_3']
        photo_4 = request.POST['photo_4']
        photo_5 = request.POST['photo_5']
        photo_6 = request.POST['photo_6']
        photo_7 = request.POST['photo_7']
        photo_8 = request.POST['photo_8']
        photo_9 = request.POST['photo_9']
        photo_10 = request.POST['photo_10']
        photo_11 = request.POST['photo_11']
        property = Property.objects.create(owner=owner, title=title, address=address, city=city,
                                state=state, zipcode=zipcode, description=description,
                                price=price, bedrooms=bedrooms, bathrooms=bathrooms,
                                garage=garage, sqft=sqft, lot_size=lot_size, photo_main=photo_main,
                                photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, photo_4=photo_4,
                                photo_5=photo_5, photo_6=photo_6, photo_7=photo_7, photo_8=photo_8,
                                photo_9=photo_9, photo_10=photo_10, photo_11=photo_11)
        property.save()
        messages.success("You have successfully posted the property!")
        return redirect("properties:properties")
    else:
        return render(request, 'properties/add-property.html')


