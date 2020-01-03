from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from core.helpers import getUniqueId, LongUniqueId


class MainPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(verbose_name="Main Image", blank=True, null=True, upload_to='pages/img', help_text="Image size should be 922x731 px")
    body = RichTextField(blank=True, null=True)
    vid_file = models.FileField(upload_to='blog/videos', blank=True, null=True, help_text="Upload Video File")
    youtube_video_id = models.CharField(blank=True, null=True, max_length=20, help_text="Youtube Video ID e.g L0I7i_lE5zA. Not Complete Url")
    extra_info = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    on_navigation = models.BooleanField(default=False)
    # Metadata 
    class Meta: 
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Pages'
        ordering = ["-title", ]
    # Methods
    def get_video_link(self):
        if self.youtube_video_id:
            return "https://www.youtube.com/embed/{}".format(self.youtube_video_id)
        elif self.vid_file:
            return self.vid_file.url
        else:
            return None
    def __str__(self):
        return self.title


class HomePageSlider(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    class Meta: 
        verbose_name = 'Home Page Slider'
        verbose_name_plural = 'Home Page Sliders'
        ordering = ["-updated", ]

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    slider = models.ForeignKey(HomePageSlider, on_delete=models.CASCADE, related_name='sliders')
    file = models.ImageField(upload_to='sliders/img', help_text="Image size is 1900px width and 1267px height")
    header = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    button_1 = models.CharField(max_length=50, blank=True, null=True)
    button_1_url = models.CharField(max_length=100, blank=True, null=True)
    button_2 = models.CharField(max_length=50, blank=True, null=True)
    button_2_url = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    class Meta: 
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'
        ordering = ["-updated", ]
    def __str__(self):
        return self.slider.title
 
class Partner(models.Model):
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='partners', help_text='Image size is 340x145 px')
    website = models.CharField(max_length=200, help_text="Start with http:// or https://")

    def __str__(self):
        return self.title

class SiteInformation(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    info = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)

    class Meta: 
        verbose_name = 'Site Information'
        verbose_name_plural = 'Site Informations'
        ordering = ["-updated", ]

    def __str__(self):
        return self.title


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics', help_text="Image size is 270x308 px")
    address = models.CharField(blank=True, null=True,  max_length=20,)
    bio = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    gender = models.CharField(default="Others", blank=True, null=True, max_length=6, help_text="Gender", choices=GENDER)
    dob = models.DateField(blank=True, null=True,help_text='Date of Birth')
    one_click_purchasing = models.BooleanField(default=False)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"
        ordering = ["-reg_date",]

    def __str__(self):
        return self.user.username



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

class Address(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.user.user.username} - {self.street_address[:10]}' # self.user.user.username

