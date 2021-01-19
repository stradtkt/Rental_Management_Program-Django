from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'properties/properties.html', context)
