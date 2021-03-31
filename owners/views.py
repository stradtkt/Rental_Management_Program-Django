from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Review
from properties.models import Property


class OwnerListView(ListView):
    fields = ("name", "email", "photo", "description", "phone", "reviews")
    model = Owner
    context_object_name = "owners"
    template_name = "owners/owners.html"


def owner_detail(request, pk):
    owner = Owner.objects.get(id=pk)
    properties = Property.objects.filter(owner=owner).order_by('-price')[:3]
    reviews = Review.objects.filter(owner=owner).order_by('-stars')[:4]
    # if request.method == 'POST':
    #     owner = request.POST['owner']
    #     title = request.POST['title']
    #     description = request.POST['description']
    #     stars = request.POST['stars']
    #     review = Review
    context = {
        "owner": owner,
        "properties": properties,
        "reviews": reviews,
    }
    return render(request, "owners/profile.html", context)


class ReviewCreateView(CreateView):
    fields = ("owner", "title", "description", "stars")
    model = Review

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.pk
        return initial