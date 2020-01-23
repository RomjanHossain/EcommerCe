from django.shortcuts import render, get_object_or_404
from django.http import Http404
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
    # try:
    #     instance = Product.objects.get(id=pk)
    #     print(instance)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product does not Exists")
    # instance = Product.objects.get(id=pk)
    # if instance is None:
    #     raise Http404("Object dones not exists")
    # return instance

    context = {
        'object': instance
    }
    return render(request, "product/detail.html", context)


def featured_view(request, pk=None, *args, **kwargs):
    try:
        obj = Product.objects.get(id=pk, featured=True)
    except Product.DoesNotExist:
        print('this is not featured')
        obj = ''
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', context)


def slug_view(request, slug, *args, **kwargs):
    instance = get_object_or_404(Product, slug=slug)
    context = {
        'object': instance
    }
    return render(request, "product/detail.html", context)
