from . import views
from django.urls import path

urlpatterns = [
    path('', views.monster_library, name='monster_library'),
]