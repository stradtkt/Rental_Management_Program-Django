from django.urls import path
from django.conf.urls import url
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/$', views.HomePageDetailsView.as_view(), name='detail'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-of-agreement/', views.terms, name='terms'),
]