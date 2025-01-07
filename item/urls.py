from . import views
from django.urls import path

urlpatterns = [
    path('', views.item_list, name='item_list'),
]