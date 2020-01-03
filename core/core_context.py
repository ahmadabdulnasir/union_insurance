from .helpers_sub import getSitePhone, getSiteEmail, getSiteAddress, getSiteSocial, getSiteTagline, DaboLinux
#from academics.models import Subject
from django.shortcuts import render_to_response



def UniversalContext(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    context = {}
    context['phone'] = getSitePhone()
    context['email'] = getSiteEmail()
    context['address'] = getSiteAddress()
    context['phones'] = getSitePhone(3)
    context['facebook'] = getSiteSocial('facebook')
    context['twitter'] = getSiteSocial('twitter')
    context['linkedin'] = getSiteSocial('linkedin')
    context['instagram'] = getSiteSocial('instagram')
    context['youtube'] = getSiteSocial('youtube')
    context['tagline'] = getSiteTagline()
    context['provider'] = DaboLinux()
    egg = True if request.user.is_superuser else False
    print('[DEBUG]: User is admin: ', egg)
    context['is_admin'] = egg
    return context

