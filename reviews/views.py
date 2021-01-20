from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'reviews/reviews.html', context)
