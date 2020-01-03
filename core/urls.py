from django.urls import path
from .views import (
    HomeView,
    MainPageDetailView,
    contactView,
)

# app_name = 'core'

urlpatterns = [
    path('p/<str:slug>/', MainPageDetailView.as_view(), name='page'),
    path('contact/', contactView, name='contact'),
    path('', HomeView.as_view(), name='home'),
]
