from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),

    # 添加/🏔删除到购物车
    url(r'^addtoCart/', views.addtoCart, name='addtoCart'),
    url(r'^subtoCart/', views.subtoCart, name='subtoCart'),

    # 添加/减少购物车中的商品
    url(r'^addCart/', views.addCart, name='addCart'),
    url(r'^subCart/', views.subCart, name='subCart'),

    # 改变选中状态
    url(r'^changeStatus/', views.changeStatus, name='changeStatus'),

    # 查看全选
    url(r'^allSelect/', views.allSelect, name='allSelect')
]
