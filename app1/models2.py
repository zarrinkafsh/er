from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)

class ProductVersion(models.Model):
    product_version_code = models.IntegerField()
    release_date = models.DateTimeField()
    description = models.TextField()
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)

class ProductFeatures(models.Model):
    product_feature_name = models.CharField(max_length=200)
    product_feature_code = models.CharField(max_length=200)
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)

class ProductVersionDetails(models.Model):
    product_version_id = models.ForeignKey('ProductVersion', on_delete=models.CASCADE)
    product_version_id = models.ForeignKey('ProductFeatures', on_delete=models.CASCADE)

class ProductSuites(models.Model):
    product_suite_name = models.CharField(max_length=200)
    product_suite_code = models.CharField(max_length=200)
    product_version_id = models.ForeignKey('productVersion', on_delete=models.CASCADE)#problem

class ActiveFeatures(models.Model):
    product_suite_id = models.ForeignKey('productSuites', on_delete=models.CASCADE)
    feature_id = models.ForeignKey('productFeatures', on_delete=models.CASCADE)

class ProductBundle(models.Model):
    concurrent_user_count = models.IntegerField()
    product_suit_id = models.ForeignKey('productSuites', on_delete=models.CASCADE)
    online_check = models.BooleanField()



class Customers(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_code = models.CharField(max_length=200)
    description = models.TextField()

class Contracts(models.Model):
    contract_code = models.CharField(max_length=200)
    customer_id = models.ForeignKey('Customers', on_delete=models.CASCADE)
    contract_attachment = models.TextField() #####################

class ContractDetails(models.Model):
    contract_id = models.ForeignKey('Contracts', on_delete=models.CASCADE)
    product_bundle_id = models.ForeignKey('productBundle', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    support_start_time = models.DateTimeField()
    support_end_time = models.DateTimeField()
    description = models.TextField()

class LicenseKeys(models.Model):
    contract_detail_id = models.ForeignKey('ContractDetails', on_delete=models.CASCADE)
    TYPES = [
        ('1','type1'),
        ('2','type2'),
        ('3','type3'),
    ]
    license_type = models.CharField(
        max_length=1,
        choices=TYPES,
        default='1',
    )
    key = models.CharField(max_length=200)
    STATUS = [
        ('1', 'active'),
        ('0', 'inactive'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='1',
    )




###
