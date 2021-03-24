from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path('', views.FindAHomeListView.as_view(), name='homes'),
]