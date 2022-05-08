from django.http import JsonResponse
from django.shortcuts import render

from cart.models import AxfCart
from cart.views import get_total_price
from order.models import AxfOrder, AxfOrderGoods


def order_detail(request):
    order_id = request.GET.get('order_id')

    order = AxfOrder.objects.get(pk=order_id)

    context = {
        'order': order,
        'price': order.axfordergoods_set.first().og_total_price
    }

    return render(request, 'axf/order/order_detail.html', context=context)


def make_order(request):
    user_id = request.session.get('user_id')

    order = AxfOrder()
    order.o_user_id = user_id
    order.save()

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    for cart in carts:
        orderGoods = AxfOrderGoods()
        orderGoods.og_goods = cart.c_goods
        orderGoods.og_order = order
        orderGoods.og_goods_num = cart.c_goods_num
        orderGoods.og_total_price = get_total_price(user_id)
        orderGoods.save()
        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }
    return JsonResponse(data=data)
