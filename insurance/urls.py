from django.urls import path
from .views import InsuranceListView, InsuranceDetailView, paymentView

urlpatterns = [
	path('insurance/<slug>/', InsuranceDetailView.as_view(), name='details'),
	path('payment/', paymentView, name='payment'),
	path('', InsuranceListView.as_view(),  name='list'),
]