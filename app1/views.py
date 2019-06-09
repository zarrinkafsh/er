from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from . import forms, models, tables
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from datetime import datetime


def index(request):
    if request.method == 'POST':
        print(request.POST)
    form = forms.Productform()
    list = models.Products.objects.all()
    fields = ['Product Name','Product Code']
    return render(request, 'app1/index0.html',
                        {'form': form,'list':list,
                        'fields':fields})

def products(request):
    list = models.Products.objects.all()
    fields = ['ProductName','ProductCode']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Products',
    'purl':'app1:product'}
    if request.method == 'POST':
        form = forms.Productform(request.POST)
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
    form = forms.Productform()
    con['form']=form
    return render(request, 'app1/product.html',con)

def customers(request):
    list = models.Customers.objects.all()
    fields = ['customer name','customer code', 'description']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Customers',
    'purl':'app1:customer'}
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


def products_version(request):
    print('version')
    list = models.ProductVersion.objects.all()
    fields = ['version code','release date', 'description', 'product']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Product Version',
    'purl':'app1:product_version'}
    if request.method == 'POST':
        form = forms.ProductVersionform(request.POST)
        print('time',
                    request.POST['product_version_code'],
                    request.POST['product_id'],
                    request.POST['description'])
        produc = models.Products.objects.get(pk=request.POST['product_id'])
        obj = models.ProductVersion()
        obj.description = request.POST['description']
        obj.product_version_code = int(request.POST['product_version_code'])
        obj.product_id = produc
        dat = request.POST.get('release_date')
        obj.release_date = dat
        obj.save()
    form = forms.ProductVersionform()
    con['form']=form
    return render(request, 'app1/product_version.html',con)


def products_feature(request):
    list = models.ProductFeatures.objects.all()
    fields = ['feature name','feature code','product']
    con ={'list':list,'fields':fields,'table_name':'Add/edit Product Feature',
    'purl':'app1:product_feature'}
    if request.method == 'POST':
        form = forms.ProductFeatureform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = models.ProductFeatures()
            obj.product_feature_name = cd['product_feature_name']
            obj.product_feature_code = cd['product_feature_code']
            produc = models.Products.objects.get(pk=request.POST['product_id'])
            obj.product_id = produc
            obj.save()
            print('ok')
            con['massage']='ok'
        else:
            con['massage']='not ok'
    form = forms.ProductFeatureform()
    con['form']=form
    return render(request, 'app1/product_feature.html',con)


def products_version_detail(request):
    print('version detail')
    list = models.ProductVersionDetails.objects.all()
    fields = ['version id','feature id']
    table = tables.ProductVersionDetailsTable(list)
    con ={'list':list,'table':table,
        'table_name':'Add/edit Product Version Detail',
        'purl':'app1:product_version_detail'}
    if request.method == 'POST':
        form = forms.ProductVersionDetailform(request.POST)
        if form.is_valid():
            product_vesion = models.ProductVersion.objects.get(pk=request.POST['product_version_id'])
            product_feature = models.ProductVersion.objects.get(pk=request.POST['product_feature_id'])
            obj = models.ProductVersionDetails()
            obj.product_version_id = product_vesion
            obj.product_feature_id = product_feature
            obj.save()
            con['massage']='ok'
        else:
            con['massage']='not ok'
    form = forms.ProductVersionDetailform()
    con['form']=form
    return render(request, 'app1/all.html',con)






##
