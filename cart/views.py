from django.shortcuts import render
from .models import Cart
# Create your views here.


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New Cart created')
    return cart_obj


def cart(request):
    request.session['cart_id'] = "12"
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            print('Cart ID exists')
            cart_obj = qs.first()
        else:
            cart_obj = cart_create()
            request.session['cart_id'] = cart_obj.id
    # print(dir(request.session))
    # request.session['name'] = 'fuck who cares'
    return render(request, 'cart/carts.html', {})
