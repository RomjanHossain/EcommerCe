from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
# Create your views here.


class ProductView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/prod.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, 'product/prod.html', context)
