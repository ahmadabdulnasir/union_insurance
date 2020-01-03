from django.contrib import admin

from .models import Address, UserProfile
from .models import MainPage, HomePageSlider, SliderImage, Partner, SiteInformation



class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'on_navigation')
    search_fields = ['title', 'sub_title', 'body']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["pub_date","updated"]

class SliderInline(admin.TabularInline):
    model = SliderImage



class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderInline]
    class Meta:
        model = HomePageSlider

class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ['title', 'verifycode','slug']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["timestamp","updated"]


class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ( 'user', 'name', 'dob', 'active')
    search_fields = ['user__username', 'gender', 'phone_number']

    class Meta:
    	model = UserProfile

    def name(self, obj):
    	return str(obj.user.first_name)+" "+ str(obj.user.last_name)

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip_code',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user__user__username', 'street_address', 'apartment_address', 'zip_code']


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(HomePageSlider, SliderAdmin)  
admin.site.register(Partner)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(SiteInformation, SiteInformationAdmin)