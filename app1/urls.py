from django.urls import path, re_path
from . import views

app_name='app1'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products/$', views.products, name='products'),
    re_path(r'^customers/$', views.customers, name='customers'),

]
