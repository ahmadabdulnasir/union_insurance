from django.urls import path
from .views import ( DashboardView, ProfileView,
)

# app_name = 'core'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', DashboardView.as_view(), name='index'),
]
