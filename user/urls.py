from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册账号
    url(r'^zc/', views.zc, name='zc'),

    # 检验姓名
    url(r'^checkname/', views.checkname, name='checkname'),

    # 验证码
    url(r'^get_code/', views.get_code, name='get_code'),

    # 登陆
    url(r'^login/', views.login, name='login'),

    # 退出
    url(r'^loginout/', views.loginout, name='loginout')

]
