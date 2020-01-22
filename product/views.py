from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    print(context['qs'])
    return render(request, 'product/prod.html', context)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "product/detail.html", context)
