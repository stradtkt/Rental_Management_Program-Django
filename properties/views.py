from django.shortcuts import render
from properties.models import Property

def index(request):
    properties = Property.objects.order_by('-address').all()
    context = {
        "properties": properties
    }
    return render(request, 'properties/properties.html', context)


