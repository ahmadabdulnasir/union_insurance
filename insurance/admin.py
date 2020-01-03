from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Insurance, InsuranceType, Payment


class InsuranceTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'timestamp', 'featured', 'active', ]
    search_fields = ['title', 'slug', 'timestamp', 'updated']
    list_filter = ['featured', 'label', 'timestamp', 'updated'] 

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['client', 'ref_id', 'insurance_type', 'start_date', 'end_date', 'paid', 'payment_ref', 'active', ]
    search_fields = ['client', 'ref_id', 'start_date', 'insurance_type__title', 'payment_ref']
    list_filter = ['insurance_type', 'start_date', 'end_date', 'timestamp', 'active'] 


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'reference', 'transaction_id', 'status', 'amount', 'success', 'timestamp' ]
    search_fields = ['insurance__client', 'transaction_id', 'reference',]
    list_filter = ['timestamp', 'success'] 


# Register your models here.
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(InsuranceType, InsuranceTypeAdmin)
admin.site.register(Payment, PaymentAdmin)