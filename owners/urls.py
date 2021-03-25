from django.urls import path
from django.conf.urls import url
from . import views

app_name = "owners"
urlpatterns = [
    path('', views.OwnerListView.as_view(), name="owners"),
    url(r'^(?P<pk>\d+)/$', views.OwnerDetailView.as_view(), name='profile'),
]