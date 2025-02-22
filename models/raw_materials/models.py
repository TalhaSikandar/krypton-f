from django.db import models
from django.utils import timezone

# Create your models here.

class Rawmaterial(models.Model):

    rawmaterial_name = models.CharField(max_length=200, blank=False, null=False, help_text="Raw Material Name")
    description = models.TextField(blank=True, null=True, help_text="RawMaterial Description")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class units(models.TextChoices):
            NORMAL = "NORMAL", "Normal"
            KG = "KG", "Kilogram"
            CM = "CM", "Centimeter"
            LITRE = "LITRE", "Litre"
    unit_weight = models.CharField(max_length=10, default=units.NORMAL, choices=units.choices, blank=False, null=False, help_text="Enter the measuring weight for raw_material")
    price = models.PositiveIntegerField(default=0, blank=False, null=False, help_text="enter price per unit")



    class Meta:
        ordering = ['rawmaterial_name']
        verbose_name_plural = 'Raw Materials'


        # related to admin page
    def __str__(self):
        return self.rawmaterial_name
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('rawmaterial-detail-view', args=[str(self.id)])
