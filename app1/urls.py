from django.urls import path, re_path
from . import views

app_name='app1'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products/$', views.products, name='products'),
    re_path(r'^customers/$', views.customers, name='customers'),
    re_path(r'^product_version/$', views.products_version, name='products_version'),
    re_path(r'^product_feature/$', views.products_feature, name='products_feature'),

]
