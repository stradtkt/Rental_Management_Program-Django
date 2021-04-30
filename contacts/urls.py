from django.conf.urls import url
from . import views

app_name = "contacts"

urlpatterns = [
    url('^$', views.index, name="contacts"),
]