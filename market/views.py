from django.shortcuts import render

# Create your views here.
from market.models import AxfFoodType, AxfGoods


def market(request):
    foodtypes = AxfFoodType.objects.all()

    typeid = request.GET.get('typeid', '104749')

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    childtypename_list = childtypenames.split('#')

    child_type_name = []
    for childtypename in childtypename_list:
        childtype_name = childtypename.split(':')  # [0]
        child_type_name.append(childtype_name)

    Goods = AxfGoods.objects.filter(categoryid=typeid)

    childcid = request.GET.get('childcid', '0')

    if childcid == '0':
        pass
    else:
        Goods = Goods.filter(childcid=childcid)

    sort_rule_list = [
        ['综合排序', '0'],
        ['价格升序', '1'],
        ['价格降序', '2'],
        ['销量升序', '3'],
        ['销量降序', '4'],
    ]

    sortrule = request.GET.get('sortrule', '0')

    if sortrule == '0':
        pass
    elif sortrule == '1':
        Goods = Goods.order_by('price')
    elif sortrule == '2':
        Goods = Goods.order_by('-price')
    elif sortrule == '3':
        Goods = Goods.order_by('productnum')
    else:
        Goods = Goods.order_by('-productnum')

    context = {
        'foodtypes': foodtypes,
        'Goods': Goods,
        'typeid': typeid,
        'child_type_name': child_type_name,
        'childcid': str(childcid),
        'sort_rule_list': sort_rule_list,
        'sortrule': sortrule,
    }

    return render(request, 'axf/main/market/market.html', context=context)
