import re

from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from user.models import AxfUser

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.utils.six import BytesIO
from axf import settings


def zc(request):
    if request.method == 'GET':
        return render(request, 'axf/user/zc.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        user = AxfUser()
        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon
        user.save()
        return render(request, 'axf/user/login.html')


def checkname(request):
    name = request.GET.get('name')
    checkusername = AxfUser.objects.filter(u_name=name)
    data = {
        'status': 200,
        'msg': '用户名可以使用'
    }
    if checkusername.count() > 0:
        data['msg'] = '该用户名已存在'
        data['status'] = 201
    return JsonResponse(data=data)


def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def login(request):
    if request.method == 'GET':
        return render(request, 'axf/user/login.html')
    if request.method == 'POST':
        # 用户输入的验证码
        imgcode = request.POST.get('imgcode')
        # 所有的验证码都会把验证码的值写到session上
        verify_code = request.session.get('verify_code')

        # 不区分大小写 search和match没有区别
        b = re.search(imgcode, verify_code, re.IGNORECASE)
        if b:
            name = request.POST.get('name')
            users = AxfUser.objects.filter(u_name=name)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')
                if password == user.u_password:
                    request.session['user_id'] = user.id
                    return redirect(reverse('axfmine:mine'))
                else:
                    msg = '密码不正确'
                    return render(request, 'axf/user/login.html', context=locals())
            else:
                msg = '用户名不存在'
                return render(request, 'axf/user/login.html', context=locals())
        else:
            msg = '验证码错误'
            return render(request, 'axf/user/login.html', context=locals())


def loginout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))
