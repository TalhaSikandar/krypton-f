# from enum import unique
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db import models
# from contacts.models import Contact, Address
# from django.utils import timezone
# Create your models here.
# companies/models.py

from django.db import models
from contacts.models import Contact, Address
from django.utils import timezone

class Company(models.Model):
    company_name = models.CharField(max_length=200, unique=False, blank=False, null=False, help_text="Company Name")
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, blank=True, null=True, related_name="companies")
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name="companies")
    website = models.URLField(max_length=200, blank=True, null=True, help_text="Company Website")
    industry = models.CharField(max_length=100, blank=True, null=True, help_text="Industry")
    description = models.TextField(blank=True, null=True, help_text="Company Description")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company-detail-view', args=[str(self.id)])
# class Company(models.Model):
#     company_name = models.CharField(max_length=200,unique=False, blank=False, null=False, help_text="Company Name")
#     contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, blank=True, null=True, related_name="companies")
#     address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name="companies")
#     created_at = models.DateTimeField(default=timezone.now, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)
#     # company_code = models.PositiveBigIntegerField(validators=[
#     #                                             MinValueValidator(10), MaxValueValidator(10)
#     #                                               ], blank=False, null=False, unique=True)
#     # company_code = models.CharField(max_length=10, blank=False, null=False, unique=False)
#
#     class Meta:
#         ordering = ['company_name']
#         verbose_name_plural = 'Companies'
#
#
#         # related to admin page
#     def __str__(self):
#         return self.company_name
#     def get_absolute_url(self):
#         """Returns the URL to access a particular instance of MyModelName."""
#         return reverse('model-detail-view', args=[str(self.id)])
#
#
