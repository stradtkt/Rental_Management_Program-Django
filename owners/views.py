from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Review
from accounts.models import User
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
    context = {
        "owner": owner,
        "properties": properties,
        "reviews": reviews,
    }
    return render(request, "owners/profile.html", context)


def create_review(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['id'])
        owner = Owner.objects.get(id=id)
        title = request.POST['title']
        description = request.POST['description']
        stars = request.POST['stars']
        if user is not None:
            Review.objects.create(user=user, owner=owner, title=title, description=description, stars=stars)
            messages.success(request, "Review added!")
            return redirect("owners:profile")
        else:
            messages.error(request, "You need to be logged in to write a review!")
            return redirect("accounts:login")
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