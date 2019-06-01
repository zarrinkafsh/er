from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from . import forms, models
from django.views.decorators.csrf import csrf_protect
from django.views import generic



def index(request):
    form = forms.aa()
    list = models.Products.objects.all()
    fields = ['Product Name','Product Code']
    return render(request, 'app1/index.html',
                        {'form': form,'list':list,
                        'fields':fields})

def products(request):
    list = models.Products.objects.all()
    fields = ['ProductName','ProductCode']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Products'}
    if request.method == 'POST':
        form = forms.aa(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = models.Products()
            obj.product_name = cd['product_name']
            obj.product_code = cd['product_code']
            obj.save()
            print('ok', cd['product_name'])
            con['massage']='ok'
        else:
            con['massage']='not ok'
    form = forms.aa()
    con['form']=form
    return render(request, 'app1/product.html',con)

def customers(request):
    list = models.Customers.objects.all()
    fields = ['customer name','customer code', 'description']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Customers'}
    if request.method == 'POST':
        form = forms.Customerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = models.Customers()
            obj.customer_name = cd['customer_name']
            obj.customer_code = cd['customer_code']
            obj.description = cd['description']
            obj.save()
            con['massage']='ok'
        else:
            con['massage']='not ok'
    form = forms.Customerform()
    con['form']=form
    return render(request, 'app1/customers.html',con)







##
