from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import validators
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    contact_no = models.CharField(max_length=11,blank=True, null=True, help_text="Enter contact no")
    email = models.EmailField(max_length=254, help_text="Enter email")
    website = models.URLField(unique=False, default='', max_length=200, blank=True, null=True, help_text="Enter your website url")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['contact_no']
        verbose_name_plural = "Contacts"


        # related to admin page
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

class Address(models.Model):
    city = models.CharField(max_length=50, blank=False, null=False, help_text="Enter City")
    country = models.CharField(max_length=50, blank=False, null=False, help_text="Enter Country")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ['country']
        verbose_name_plural = "Addresses"
        # related to admin page
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
