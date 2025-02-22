from django.db import models
from django.utils import timezone
from contacts.models import Contact, Address
from companies.models import Company
from products.models import Product

# Create your models here.

class Warehouse(models.Model):

    warehouse_name = models.CharField(max_length=200, blank=False, null=False, help_text="WareHouse Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True, through='WarehouseProduct', related_name="warehouses") # to make a new column amount used through ...
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(default='', null=False)



    class Meta:
        ordering = ['warehouse_name']
        verbose_name_plural = 'warehouses'


        # related to admin page
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('warehouse', args=[str(self.id)])

class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField(null=False, default=0, blank=True, help_text="Quantity Available in warehouse")
