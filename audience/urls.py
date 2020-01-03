from django.conf.urls import url, include

from .views import contactView, subscriberView

# from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'contact/$', contactView,  name='contact'),
	url(r'subscribe/$', subscriberView, name='add-subscriber'), 
]
 
