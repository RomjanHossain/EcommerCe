from django.shortcuts import render
from product.models import Product
from tags.models import SearchTags
from django.db.models import Q
# Create your views here.


def search_product_list_view(request):
    # queryset = Product.objects.filter(title__icontains="head")
    # print(context['qs'])
    query = request.GET.get('q')
    print(query)
    if query is not None:
        lookups = Q(title__icontains=query) | Q(
            description__icontains=query) | Q(searchtags__title__icontains=query)
        searched = Product.objects.filter(lookups).distinct()
    else:
        searched = Product.objects.filter(featured=True)

    context = {
        'qs': searched,
        'searched': query
    }
    return render(request, 'search/searched.html', context)
