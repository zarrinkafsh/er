import django_tables2 as tables
from . import models
class ProductVersionDetailsTable(tables.Table):
    class Meta:
        model = models.ProductVersionDetails
        attrs = {'class': 'table table-sm'}
