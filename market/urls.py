from django.conf.urls import url

from market import views

urlpatterns = [
    url('^market/', views.market, name='market'),
]
