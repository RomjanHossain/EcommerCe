from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_product_list_view, name='search'),
]
