from django.shortcuts import render
from . import models
from owners.models import Owner

def index(request):
    context = {}
    return render(request, 'contacts/contacts.html', context)
