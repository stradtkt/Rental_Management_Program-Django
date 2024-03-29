from django.conf.urls import url
from . import views

app_name = "owners"
urlpatterns = [
    url('^$', views.owners, name="owners"),
    url(r'^(?P<id>\d+)/create-review/$', views.create_review, name="create_review"),
    url(r'^(?P<pk>\d+)/$', views.owner_detail, name='profile'),
]