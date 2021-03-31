from django.urls import path
from django.conf.urls import url
from . import views

app_name = "owners"
urlpatterns = [
    path('', views.OwnerListView.as_view(), name="owners"),
    path('create/', views.ReviewCreateView.as_view(), name='create_review'),
    url(r'^(?P<pk>\d+)/$', views.owner_detail, name='profile'),
]