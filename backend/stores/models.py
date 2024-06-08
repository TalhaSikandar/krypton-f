from django.db import models
from django.utils import timezone
from contacts.models import Contact, Address
from companies.models import Company
from django.conf import settings
from products.models import Product

# Create your models here.

class Store(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, related_name="stores")
    # manager = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=False, null=True, related_name="stores")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=False, null=True, related_name="stores")
    products = models.ManyToManyField(Product, blank=True, through='StoreProduct', related_name="stores") # to make a new column amount used through ...
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True, related_name="stores")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name="stores")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(default='', null=False)

    # Add the slug field later for     
    # Add prefetch related in the views for relationsurls

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Stores'


        # related to admin page
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
class StoreProduct(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField(null=False, default=0, blank=True, help_text="Total Products Available in store")
