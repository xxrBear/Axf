from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order_detail/', views.order_detail, name='order_detail'),

    # 制造订单
    url(r'^make_order/', views.make_order, name='make_order')
]
