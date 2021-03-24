from django.urls import path
from django.conf.urls import url
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/$', views.HomePageDetailsView.as_view(), name='detail'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]