from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Review
from accounts.models import User
from properties.models import Property


def owners(request):
    owners = Owner.objects.all().order_by("name")
    context = {
        "owners": owners,
    }
    return render(request, "owners/owners.html", context)


def owner_detail(request, pk):
    owner = Owner.objects.get(id=pk)
    properties = Property.objects.filter(owner=owner).order_by('-price')[:3]
    reviews = Review.objects.filter(owner=owner).order_by('-stars')[:4]
    context = {
        "owner": owner,
        "properties": properties,
        "reviews": reviews,
    }
    return render(request, "owners/profile.html", context)


def create_review(request, id):
    if request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        owner = Owner.objects.get(id=id)
        title = request.POST['title']
        description = request.POST['description']
        stars = request.POST['stars']
        Review.objects.create(user=user, owner=owner, title=title, description=description, stars=stars)
        messages.success(request, "Review added!")
        return redirect('/owners/{}/'.format(id))
    else:
        return render(request, "owners/profile.html")

# class ReviewCreateView(CreateView):
#     fields = ("owner", "title", "description", "stars")
#     model = Review
#
#     def get_initial(self):
#         initial = super().get_initial()
#         initial['user'] = self.request.user.pk
#         return initial