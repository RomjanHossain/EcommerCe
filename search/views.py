from django.shortcuts import render
from product.models import Product
# Create your views here.


def search_product_list_view(request):
    # queryset = Product.objects.filter(title__icontains="head")
    # print(context['qs'])
    query = request.GET.get('q')
    print(query)
    if query is not None:
        searched = Product.objects.filter(title__icontains=query)
    else:
        searched = Product.objects.filter(featured=True)

    context = {
        'qs': searched,
        'searched': query
    }
    return render(request, 'search/searched.html', context)
