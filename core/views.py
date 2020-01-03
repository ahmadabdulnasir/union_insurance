from django.views.generic import ListView, DetailView
from .helpers_sub import Egg, themeVersion, getSiteMedia
# from shop.models import Item, ProductCategory
from .models import MainPage, HomePageSlider
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from insurance.models import InsuranceType


# Create your views here.
class HomeView(ListView):
    model = InsuranceType
    paginate_by = 12
    template_name = "core/home.html"
    def get_context_data(self, *args, **kwargs):  
        try:            
            context = super(HomeView, self).get_context_data(*args, **kwargs)
            context['slider'] = HomePageSlider.objects.filter(active=True).first()
            return context
        except MainPage.DoesNotExist as e:
            print('[Error]: ', )
        except Exception as e:
            print('[Error]: ', )


class MainPageDetailView(DetailView):
    template_name = "core/pages.html" #.format(themeVersion() )
    model = MainPage
    query_pk_and_slug = True
    context_object_name = 'page'
    # context = {}
    def get_context_data(self, *args, **kwargs):  
        try:            
            context = super(MainPageDetailView, self).get_context_data(*args, **kwargs)
            return context
        except MainPage.DoesNotExist:
            context['page'] =  Egg
            #TODO: send mail on error
            print('Not Found')
            return context
        return context

def contactView(request):
    next_url = reverse('audience:contact')
    return HttpResponseRedirect(next_url)
