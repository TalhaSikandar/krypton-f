from django.db import models
from django.utils import timezone
from raw_materials.models import Rawmaterial

# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=200, blank=False, null=False, help_text="Product Name")
    raw_materials = models.ManyToManyField(Rawmaterial, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['product_name']
        verbose_name_plural = 'products'


        # related to admin page
    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
