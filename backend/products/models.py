from django.db import models
from django.utils import timezone
from raw_materials.models import Rawmaterial

# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=200, blank=False, null=False, help_text="Product Name")
    raw_materials = models.ManyToManyField(Rawmaterial, blank=True, related_name="products", through="ProductRawMaterial")
    description = models.TextField(blank=True, null=True, help_text="Product Description")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class units(models.TextChoices):
            NORMAL = "NORMAL", "Normal"
            KG = "KG", "Kilogram"
            CM = "CM", "Centimeter"
            LITRE = "LITRE", "Litre"
    unit_weight = models.CharField(max_length=10, default=units.NORMAL, choices=units.choices, blank=False, null=False, help_text="Enter the measuring weight for product")



    class Meta:
        ordering = ['product_name']
        verbose_name_plural = 'products'


        # related to admin page
    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
class ProductRawmaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(Rawmaterial, on_delete=models.CASCADE)
    required_quantity = models.PositiveIntegerField(null=False, default=0, blank=True, help_text="raw material required to make the product")
