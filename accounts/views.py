from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'accounts/accounts.html', context)
