from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from cart.models import AxfCart


def cart(request):
    user_id = request.session.get('user_id')

    if user_id:

        carts = AxfCart.objects.filter(c_user_id=user_id)
        is_all_select = not AxfCart.objects.filter(c_is_select=False).exists()

        context = {
            'carts': carts,
            'price': get_total_price(user_id),
            'is_all_select': is_all_select
        }
        return render(request, 'axf/main/cart/cart.html', context=context)
    else:
        return render(request, 'axf/user/login.html')


def addtoCart(request):
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200
    }

    if user_id:
        goodsid = request.GET.get('goodis')
        carts = AxfCart.objects.filter(c_goods_id=goodsid).filter(c_user_id=user_id)

        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user_id
        cart.save()

        data['c_goods_num'] = cart.c_goods_num
        return JsonResponse(data=data)
    else:
        data['status'] = 201
        return JsonResponse(data=data)


def subtoCart(request):
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200
    }

    if user_id:
        goodsid = request.GET.get('goodis2')
        carts = AxfCart.objects.filter(c_goods_id=goodsid).filter(c_user_id=user_id)

        if carts.count() > 0:
            cart = carts.first()
            if cart.c_goods_num > 0:
                cart.c_goods_num = cart.c_goods_num - 1
            else:
                pass
        else:
            cart = AxfCart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user_id
        cart.save()

        data['c_goods_num'] = cart.c_goods_num
        return JsonResponse(data=data)
    else:
        data['status'] = 201
        return JsonResponse(data=data)


def get_total_price(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    total_prise = 0

    for cart in carts:
        total_prise = total_prise + cart.c_goods_num * float(cart.c_goods.price)

    return '%.2f' % total_prise


@csrf_exempt
def addCart(request):
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200
    }

    if user_id:
        cartid = request.POST.get('cartid')
        # print(cartid)
        cart = AxfCart.objects.get(pk=cartid)
        if cart.c_goods_num > 0:
            cart.c_goods_num = cart.c_goods_num + 1
            cart.save()
            data['c_goods_num'] = cart.c_goods_num
            price = get_total_price(user_id)
            data['price'] = price
        return JsonResponse(data=data)


@csrf_exempt
def subCart(request):
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200
    }

    if user_id:
        cartid = request.POST.get('cartid')
        # print(cartid)
        cart = AxfCart.objects.get(pk=cartid)
        if cart.c_goods_num > 1:
            cart.c_goods_num = cart.c_goods_num - 1
            cart.save()
            price = get_total_price(user_id)
            data['price'] = price
            data['c_goods_num'] = cart.c_goods_num

        else:
            cart.delete()
            data['status'] = 204
            price = get_total_price(user_id)
            data['price'] = price
            data['c_goods_num'] = cart.c_goods_num

        return JsonResponse(data=data)


def changeStatus(request):
    cartid = request.GET.get('cartid')
    user_id = request.session.get('user_id')

    data = {
        'status': 200,
        'msg': 'ok'
    }

    cart = AxfCart.objects.get(pk=cartid)
    cart.c_is_select = not cart.c_is_select
    cart.save()

    data['c_is_select'] = cart.c_is_select
    data['price'] = get_total_price(user_id)

    is_all_select = not AxfCart.objects.filter(c_is_select=False).exists()
    # print(bool(is_all_select))
    data['is_all_select'] = is_all_select
    data['price'] = get_total_price(user_id)

    return JsonResponse(data=data)


def allSelect(request):
    cartidlist = request.GET.get('cartidlist')
    cartid_list = cartidlist.split('#')
    user_id = request.session.get('user_id')
    carts = AxfCart.objects.filter(id__in=cartid_list)
    data = {
        'msg': 'ok',
        'status': 200
    }

    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()
    data['price'] = get_total_price(user_id)

    return JsonResponse(data=data)
