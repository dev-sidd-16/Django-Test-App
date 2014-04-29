from django.conf.urls import patterns, include, url
from filemanager.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^django_app/', include('django_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #user authorization urls
    url(r'^accounts/login/$', 'django_app.views.login'),
    url(r'^accounts/auth/$', 'django_app.views.auth_view'),
    url(r'^accounts/logout/$', 'django_app.views.logout'),
    url(r'^accounts/loggedin/$', 'django_app.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_app.views.invalid_login'),
    url(r'^accounts/register/$', 'django_app.views.register_user'),
    url(r'^accounts/register_success/$', 'django_app.views.register_success'),
)
