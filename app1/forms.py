from django import forms
from . import models
from datetime import datetime
from django.forms.widgets import Widget
from django.utils import timezone
from bootstrap_datepicker_plus import DatePickerInput

class Productform(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = '__all__'
        labels = {'ProductName': 'Product Name',
                    'ProductCode':'Product Code'}
        widgets = {
            'product_name': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Product Name'}),
            'product_code': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Product Code'}),
        }

class Customerform(forms.ModelForm):
    class Meta:
        model = models.Customers
        fields = '__all__'
        labels = {'ProductName': 'Product Name',
                    'ProductCode':'Product Code'}
        widgets = {
            'customer_name': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Customer Name'}),
            'customer_code': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Customer Code'}),
            'description': forms.Textarea(
                        attrs={'class': 'form-control',
                                'placeholder':'Description',
                                'rows':'4'}),
        }


from .widgets import BootstrapDateTimePickerInput
class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )

class ProductChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Name: {}".format(obj.product_name)

class ProductVersionform(forms.ModelForm):

    release_date = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
    product_id = ProductChoiceField(queryset=models.Products.objects.all(),
                                    empty_label='------no',
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))
    class Meta:
        model = models.ProductVersion
        fields = '__all__'
        labels = {'product_version_code':'Version code'}
        widgets = {
            'description': forms.Textarea(
                        attrs={'class': 'form-control',
                                'placeholder':'Description',
                                'rows':'3'}),
            'product_id': forms.Select(
                        attrs={'class': 'form-control'}),
            'product_version_code': forms.NumberInput(
                        attrs={'class': 'form-control'}),
        }


class ProductFeatureform(forms.ModelForm):
    product_id = ProductChoiceField(queryset=models.Products.objects.all(),
                                    empty_label='------no',
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))
    class Meta:
        model = models.ProductFeatures
        fields = '__all__'
        labels = {'product_feature_name': 'Feature Name',
                    'product_feature_code':'Feature Code'}
        widgets = {
            'product_feature_name': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Feature Name'}),
            'product_feature_code': forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder':'Feature Code'}),
            'product_id': forms.Select(
                        attrs={'class': 'form-control'}),
        }


class ProductVersionChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Code: {}".format(obj.product_version_code)
class ProductFeaturenChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Name: {}".format(obj.product_feature_name)

class ProductVersionDetailform(forms.ModelForm):

    product_version_id = ProductVersionChoiceField(queryset=models.ProductVersion.objects.all(),
                                    empty_label='------no',
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))

    product_feature_id = ProductFeaturenChoiceField(queryset=models.ProductFeatures.objects.all(),
                                    empty_label='------no',
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))
    class Meta:
        model = models.ProductVersionDetails
        fields = '__all__'
        labels = {'product_version_code':'Version code'}
        widgets = {
            'product_version_id': forms.Select(
                        attrs={'class': 'form-control'}),
            'product_feature_id': forms.Select(
                        attrs={'class': 'form-control'}),
        }



##
