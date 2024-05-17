from django.db import models
from django.utils import timezone
from contacts.models import Contact, Address
from companies.models import Company
from django.conf import settings

# Create your models here.

class Store(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, related_name="stores")
    manager = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=False, null=True, related_name="stores")
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True, related_name="stores")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name="stores")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # Add the slug field later for     
    # Add prefetch related in the views for relationsurls

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Stores'


        # related to admin page
    def __str__(self):
        return self.id
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
