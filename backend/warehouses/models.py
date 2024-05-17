from django.db import models
from django.utils import timezone
from contacts.models import Contact, Address
from companies.models import Company
from products.models import Product

# Create your models here.

class Warehouse(models.Model):

    warehouse_name = models.CharField(max_length=200, blank=False, null=False, help_text="WareHouse Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True)
    products = models.ManyToManyField(Product, blank=True, through='WarehouseProduct') # to make a new column amount used through ...
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['warehouse_name']
        verbose_name_plural = 'warehouses'


        # related to admin page
    def __str__(self):
        return self.warehouse_name
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0, blank=True)
