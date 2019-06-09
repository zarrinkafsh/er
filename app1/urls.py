from django.urls import path, re_path
from . import views

app_name='app1'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products/$', views.products, name='product'),
    re_path(r'^customers/$', views.customers, name='customer'),
    re_path(r'^product_version/$', views.products_version, name='product_version'),
    re_path(r'^product_version_detail/$', views.products_version_detail, name='product_version_detail'),
    re_path(r'^product_feature/$', views.products_feature, name='product_feature'),

]
