from django.urls import path
from . import views

urlpatterns = [
    path('commodities/', views.get_commodities_data, name='commodities-api'),
]