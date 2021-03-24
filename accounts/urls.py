from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.index, name="accounts"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
]