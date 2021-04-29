from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('repair', views.repair, name="repair"),
    path('store', views.store, name="store")
]
