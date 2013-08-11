from django.conf.urls.defaults import *

urlpatterns = patterns('admin.views',
     (r'^config$', 'admin'),
     (r'^my_menu/$', 'menu_admin'),
     (r'^my_pages/$', 'page_admin'),
     (r'^my_constant/$', 'const_admin'),
)
