from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       url(r'^$',direct_to_template, {'template':'main/index.html'}, name='index'),
                       url(r'^general/$','mturk.main.views.general', name='graphs_general'), 
)
