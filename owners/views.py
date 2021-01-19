from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'owners/owners.html', context)
