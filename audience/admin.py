from django.contrib import admin
from .models import ContactMessage, Subscriber, CustomerReview
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ContactMessageResource(resources.ModelResource):
    class Meta:
        model = ContactMessage
        fields = ('name', 'uid', 'email', 'date_submitted', )
        export_order = ('name', 'uid', 'email', 'subject', 'phone', 'message', 'date_submitted',)

class ContactMessageAdmin(ImportExportModelAdmin):
    resource_class = ContactMessageResource
    list_display = ['name', 'email', 'subject', 'date_submitted', ]
    search_fields = ['name', 'email', 'subject', 'date_submitted']
    list_filter = ['date_submitted',] 


class SubscriberResource(resources.ModelResource):
    class Meta:
        model = Subscriber
        fields = ('name', 'uid', 'email', 'date_registered', )
        export_order = ('name', 'uid', 'email', 'date_registered',)

class SubscriberAdmin(ImportExportModelAdmin):
    resource_class = SubscriberResource
    list_display = ['name', 'email', 'date_registered', ]
    search_fields = ['name', 'email', 'date_registered']
    list_filter = ['date_registered',]

class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'active', 'updated')
    search_fields = ['name', 'message']
    readonly_fields = ["timestamp","updated"]
    list_filter = ["timestamp","updated"]

# Register your models here.
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(CustomerReview, CustomerReviewAdmin)
