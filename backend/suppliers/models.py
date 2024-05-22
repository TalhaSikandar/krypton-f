from django.db import models
from contacts.models import Contact, Address
from django.utils import timezone
from raw_materials.models import Rawmaterial

class Supplier(models.Model):
    name = models.CharField(max_length=200, unique=False, blank=False, null=False, help_text="Supplier Name")
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, blank=True, null=True, related_name="suppliers")
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name="suppliers")
    industry = models.CharField(max_length=100, blank=True, null=True, help_text="Industry")
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
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    rawmaterial = models.ForeignKey(Rawmaterial, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, default=0, blank=True)
