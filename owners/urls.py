from django.urls import path
from django.conf.urls import url
from . import views

app_name = "owners"
urlpatterns = [
    url('^$', views.OwnerListView.as_view(), name="owners"),
    url(r'^(?P<id>\d+)/create-review/$', views.create_review, name="create_review"),
    url(r'^(?P<id>\d+)/$', views.owner_detail, name='profile'),
]