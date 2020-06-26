from django.urls import path

from cow import views

urlpatterns = [
    path('', views.index),
    path('Last10/', views.Last10),
]