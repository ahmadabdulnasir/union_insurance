from django.db import models
from core.helpers import getUniqueId, LongUniqueId
from django.utils import timezone
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
# Create your models here.


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class InsuranceType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=LongUniqueId, unique=True,)
    image = models.ImageField(verbose_name="Main Product Image")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    label = models.CharField(verbose_name="Insurance Label", max_length=10, blank=True, null=True)
    label_type = models.CharField(verbose_name="Insurance Label Type",choices=LABEL_CHOICES, default='P', max_length=1)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    featured = models.BooleanField(help_text="If the Item should be featured on homepage",default=False)
    active = models.BooleanField(default=True)

    
    class Meta:
        verbose_name = 'Insurance Type'
        verbose_name_plural = 'Insurance Types'
        ordering = ["-timestamp", "-updated", "title"]

    def get_absolute_url(self):
        return reverse("insurance:details", kwargs={
            'slug': self.slug
        })

    def get_payment_url(self):
        return reverse("insurance:payment", kwargs={
            'slug': self.slug
        })

    def get_price(self):
        try:
            if self.discount_price:
                price =self.discount_price
            else:
                price = self.price
        except Exception as e:
            price = self.price
        return price

    def amount_in_kobo(self):
        return self.get_price()*100

    def __str__(self):
        return self.title



class Insurance(models.Model):
    client = models.ForeignKey('core.UserProfile', on_delete=models.CASCADE, related_name='insurances')
    ref_id = models.CharField('Reference ID', default=getUniqueId, max_length=10, unique=True)
    insurance_type =  models.ForeignKey('insurance.InsuranceType', blank=True, null=True, on_delete=models.SET_NULL)
    # amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    paid = models.BooleanField(default=False)
    payment_ref =  models.CharField(blank=True, null=True, max_length=30)
    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'
        ordering = ["-start_date", 'ref_id']
    
    def get_amount(self):
        if self.insurance_type.get_price():
            return self.insurance_type.get_price()
        else:
            return 0

    def payMonth(self):
        return self.start_date.month
    
    # def duration(self):
    #     if self.end_date:
    #         import timedelta
    #         return self.end_date - (self.start_date.
    #     else:
    #         return "End Date not set"

    def __str__(self):
        return self.ref_id

 
class Payment(models.Model):
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False, help_text='Internal reference ID') 
    insurance = models.ForeignKey('insurance.Insurance', on_delete=models.SET_NULL, blank=True, null=True, related_name='payments')  
    reference = models.CharField(max_length=255, help_text="Reference from Paystack", blank=True, null=True,)
    transaction_id = models.CharField(max_length=255, help_text="Transaction from Paystack", blank=True, null=True,)
    message = models.CharField(max_length=255, help_text="Message from Paystack", blank=True, null=True,)
    status = models.CharField(max_length=255, help_text="Status string from Paystack", blank=True, null=True,)
    amount = models.DecimalField(max_digits=100, decimal_places=2, help_text='Amount Paid in Naira (₦)')
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, help_text="Transaction Date")

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-timestamp",]

    def get_client(self):
        return self.insurance.client

    def __str__(self):
        return str(self.uid)
