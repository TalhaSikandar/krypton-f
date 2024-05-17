from enum import unique
from django.db import models
from contacts.models import Contact, Address
from django.utils import timezone
# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200,unique=True, blank=False, null=False, help_text="Company Name")
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True)
    company_code = models.CharField(max_length=10, default="0123456789", unique=True, null=False, blank=False, help_text="Enter a 10 digit code that will be used as company code")

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'Companies'


        # related to admin page
    def __str__(self):
        return self.company_code
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])


