from django.shortcuts import render
from .models import ContactMessage, Subscriber
from django.http import HttpResponse, HttpResponseRedirect
from core.models import MainPage
from core.helpers_sub import Egg, themeVersion


def contactView(request):
    template_name = "core/contact.html" #.format(themeVersion() )
    context = {}
    if request.method == 'POST': 
        name = request.POST.get('name') 
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')        
        next_url = request.POST.get('next_url')
        try:
            msginfo = ContactMessage(name=name, email=email, subject=subject, message=message )
            msginfo.save()
            succes = ''' <script>
                        alert("Your Message, was Successfully received!");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            return HttpResponse (succes)
        except:
            error = ''' <script>
                        alert("Sorry! Your Message could not be send, Please try again later");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            return HttpResponse(error)
    try:
        page  = MainPage.objects.get(slug='contact-us')
        context['page'] = page
        return render(request, template_name, context=context) 
    except MainPage.DoesNotExist:
        context['page'] =  Egg
        return render(request, template_name, context=context) 

def subscriberView(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        next_url = request.POST.get('next_url')
        print(name, email) 
        print(next_url)
        try:
            subscriber = Subscriber(name=name, email=email )
            subscriber.save()
            succes = ''' <script>
                        alert("You have Successfully registered!");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            return HttpResponse (succes)
        except:
            error = ''' <script>
                        alert("Sorry! An Error Occur, Please try again later");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            return HttpResponse(error)
    return  HttpResponseRedirect('/')
