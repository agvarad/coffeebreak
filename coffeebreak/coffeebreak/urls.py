from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home/', }),
    (r'^(?P<offset>[\w\s]*)/$','views.Home'),
    (r'^admin/', include('admin.urls')),
    (r'^accounts/create_user/$', 'admin.views.create_new_user'),
    (r'^accounts/login/$','django.contrib.auth.views.login',{'authentication_form':AuthenticationForm,'template_name': 'login.html',}),
    (r'^(?P<offset>[\w\s]*)/(?P<detail_topic>[\w\s]*)$','views.Detail'),
)
