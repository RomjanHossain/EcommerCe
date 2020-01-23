from django.urls import path
from . import views

urlpatterns = [
    path('prod/', views.product_list_view, name='prod'),
    path('detail/<pk>', views.product_detail_view,  name='deatil'),
    path('featured/<pk>', views.featured_view, name='feature'),
    path('prod/<slug:slug>', views.slug_view, name='slugview'),
]
