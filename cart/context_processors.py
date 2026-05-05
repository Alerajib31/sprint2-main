from .models import Cart


def cart_context(request):
    ctx = {'cart_count': 0, 'cart_product_ids': set()}
    if request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'customer':
        try:
            cart = Cart.objects.get(customer=request.user)
            ctx['cart_count'] = cart.items.count()
            ctx['cart_product_ids'] = set(cart.items.values_list('product_id', flat=True))
        except Cart.DoesNotExist:
            pass
    return ctx
