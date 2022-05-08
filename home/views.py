from django.shortcuts import render

from home.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainShow


def home(request):
    wheels = AxfWheel.objects.all()

    navs = AxfNav.objects.all()

    pigs = AxfMustBuy.objects.all()

    mainshows = AxfMainShow.objects.all()

    return render(request, 'axf/main/home/home.html', context=locals())
