"""union_insurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('insurance/', include( ('insurance.urls', 'insurance'), namespace='insurance') ),
    path('dashboard/', include( ('dashboard.urls', 'dashboard'), namespace='dashboard') ),
    path('audience/', include( ('audience.urls', 'audience'), namespace='audience') ),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]


# Serve static and media files from development server
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# to make sure we capture media files before wildcard (useful in dev env only)
urlpatterns += [ path('', include( ('core.urls', 'core'), namespace='core' )) ]

admin.site.site_header = 'Union Insurance'
admin.site.index_title = 'Union Insurance Admin Interface'
admin.site.site_title = 'Union Insurance'