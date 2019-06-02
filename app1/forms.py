from django import forms
from . import models

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

class b(forms.ModelForm):
    ReleaseDate = forms.DateTimeField(
                    input_formats=['%d/%m/%Y %H:%M'],
                    widget=forms.DateTimeInput(attrs={
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'
                    })
                )
    class Meta:
        model = models.ProductVersion
        fields = '__all__'
        widgets = {
            'Description': forms.Textarea(
                        attrs={'class': 'form-control',
                                'placeholder':'Description',
                                'rows':'3'}),
            'ProductID': forms.Select(
                        attrs={'class': 'form-control'}),
            'ProductVersionCode': forms.NumberInput(
                        attrs={'class': 'form-control'}),
        }





##
