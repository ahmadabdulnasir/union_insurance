from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Insurance, InsuranceType, Payment
from django.contrib.auth.mixins import LoginRequiredMixin
from core.helpers_sub import getPaymentKey
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib import messages
# Create your views here.

class InsuranceListView(ListView):
    template_name = "insurance/insurance_list.html"
    model = InsuranceType
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InsuranceDetailView(DetailView):
    template_name = "insurance/insurance_details.html" #.format(themeVersion())
    model = InsuranceType
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment_key = getPaymentKey('paystack-key')
        context['payment_key'] = payment_key
        return context
    



def paymentView(request):
    userprofile = request.user.profile #UserProfile.objects.get(user=request.user)
    status = request.POST.get('status') 
    reference = request.POST.get('reference')
    transaction = request.POST.get('transaction')
    message = request.POST.get('message')
    insurance_slug = request.POST.get('insurance_slug') 
    next_url = request.POST.get('next_url')
    # amount = int(order.get_total() * 100)
    insurance_type = InsuranceType.objects.get(slug=insurance_slug)
    try:
        # create the payment
        payment = Payment()
        payment.user = userprofile
        payment.reference = reference
        payment.transaction_id = transaction
        payment.message = message
        payment.status = status
        payment.amount = insurance_type.get_price()
        payment.save()
        # assign the payment to the insurance
        insurance = Insurance()
        insurance.client = userprofile
        insurance.insurance_type = insurance_type
        insurance.paid = True
        insurance.start_date = timezone.now()
        insurance.payment_ref = payment.reference
        insurance.save()

        payment.insurance = insurance
        payment.save()

        messages.success(request, "Your Payment was successful!")
        # return redirect("/")
        result = {
                "message": 'Your order was successful, You will be contacted by our Sale Team Shortly',
                "next_url": '/'
            }
        return JsonResponse(result)
    except Exception as e:
        print('*'*20)
        print(e)
        print('*'*20)
        error = ''' <script>
                    alert("Sorry! There is a technical issue with your order, We have been notified");
                    window.location = "{{NEXT_URL}}";
                    </script> '''.replace("{{NEXT_URL}}", next_url)
        # TODO: send mail on failure
        messages.warning(
            request, "A serious error occurred. We have been notifed.")
        return HttpResponse(error)