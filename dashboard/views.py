from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from insurance.models import InsuranceType, Insurance
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm
from core.models import UserProfile
from django.contrib import messages

# Create your views here.
class DashboardView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        context = {}
        records = Insurance.objects.filter(client=self.request.user.profile)
        context['records'] = records

        return render(self.request, "dashboard/home.html", context)

    def post(self, *args, **kwargs):
        try:
            messages.success(self.request, "Your order was successful!")
            result = {
                    "message": 'Your order was successful, You will be contacted by our Sale Team Shortly',
                    "next_url": '/dashboard/'
                }
            return JsonResponse(result)
        except Exception as e:
            error = ''' <script>
                        alert("Sorry! There is a technical issue with your order, We have been notified");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            # TODO: send mail on failure
            messages.warning(
                self.request, "A serious error occurred. We have been notifed.")
            return HttpResponse(error)
                

        messages.warning(self.request, "Invalid data received")
        return redirect("/")

class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        context = {}
        # form = UserProfileForm()
        instance = get_object_or_404(UserProfile, user=self.request.user)
        form = UserProfileForm(instance=instance)
        context['form'] =  form
        
        return render(self.request, "dashboard/profile.html", context)

    def post(self, *args, **kwargs):
        # form = UserProfileForm(self.request.POST)
        instance = get_object_or_404(UserProfile, user=self.request.user)
        form = UserProfileForm(self.request.POST or None, instance=instance)
        if form.is_valid():
            # p_form = form.save(commit=False)
            # p_form.user = self.request.user
            # p_form.save()
            form.save()
            messages.info(self.request, "Your Profile was Updated Successfuly!!!")
            next_url = self.request.META.get('HTTP_REFERER')
            return redirect(next_url)
        else:
            return redirect("dashboard:profile")