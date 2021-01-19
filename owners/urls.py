from django.urls import path

from . import views

app_name = "owners"
urlpatterns = [
    path('', views.index, name="owners")
]