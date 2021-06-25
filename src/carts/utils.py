from . import models

def update_items_in_cart(cart_items_from_form, current_cart_pk):
    action = None
    cart = models.Cart.objects.filter(pk = current_cart_pk).first()
    if not cart:
        return
    goods = cart.goods.all()
    for name, quantity in cart_items_from_form.items():
        if name == 'btn':
            action = quantity
            continue
        item = goods.filter(pk=name).first()
        if item and int(quantity) > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    return action