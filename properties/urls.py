from django.urls import path
from django.conf.urls import url
from . import views

app_name = "properties"
urlpatterns = [
    path('', views.index, name="properties"),
    url(r'^(?P<pk>\d+)/$', views.PropertyDetailsView.as_view(), name="detail"),
]