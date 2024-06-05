from django.db import models
from contacts.models import Contact, Address
from django.utils import timezone
from raw_materials.models import Rawmaterial
from companies.models import Company

class Supplier(models.Model):
    name = models.CharField(max_length=200, unique=False, blank=False, null=False, help_text="Supplier Name")
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, blank=True, null=True, related_name="suppliers")
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name="suppliers")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True, help_text="Type of industry")
    rawmaterials = models.ManyToManyField(Rawmaterial, blank=True, through='SupplierRawmaterial', related_name="suppliers") # to make a new column amount used through ...
    description = models.TextField(blank=True, null=True, help_text="Supplier Description")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier-detail-view', args=[str(self.id)])


class SupplierRawmaterial(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplierrawmaterial")
    rawmaterial = models.ForeignKey(Rawmaterial, blank=True, on_delete=models.CASCADE, related_name="supplierrawmaterial")
    available_quantity = models.PositiveIntegerField(default=0, blank=True, help_text="available quantity supplier has")
    def __str__(self):
        return '%d: %s: %s' % (self.id, self.supplier.name, self.rawmaterial.rawmaterial_name)
    def get_absolute_url(self):
        return reverse('supplierrawmaterial-detail-view', args=[str(self.id)])
