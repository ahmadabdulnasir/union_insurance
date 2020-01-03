from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.conf import settings

# Create your models here. 

class ContactMessage(models.Model):
    """ A Class defining Contact Messages records """ 
    # Fields
    name = models.CharField(max_length=200)
    uid = models.UUIDField(default=uuid4, editable=True) 
    email = models.EmailField()
    subject = models.CharField(max_length=50, default='New Contact Us')
    phone = models.CharField(max_length=15, default='+234 ..')
    message = models.TextField()
    date_submitted = models.DateField(default=timezone.now )
 
    # Metadata 
    class Meta: 
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'
        ordering = ["-date_submitted", "name"]
    
    def __str__(self):
        return "{}".format(self.name + ' ' + self.email)

class Subscriber(models.Model):
    """  A Class defining Subscribers records """
    # Fields
    name = models.CharField(max_length=200)
    uid = models.UUIDField(default=uuid4, editable=True) 
    email = models.EmailField() 
    date_registered = models.DateField(default=timezone.now )

    # Metadata 
    class Meta:  
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ["-date_registered", "name"]
    
    def __str__(self):
        return "{}".format(self.name)

class CustomerReview(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True , related_name='reviews', on_delete=models.SET_NULL)
    img = models.ImageField(blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=True)
 
    # Metadata 
    class Meta: 
        verbose_name = 'Customer Review'
        verbose_name_plural = 'Customers Reviews'
        ordering = ["-updated", "-timestamp","name"]
    
    def __str__(self):
        return self.name