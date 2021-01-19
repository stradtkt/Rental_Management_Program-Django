from django.urls import path

from . import views

app_name = "renters"
urlpatterns = [
    path('', views.index, name="renters")
]