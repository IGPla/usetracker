# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from usetracker import views

urlpatterns = [
    url(r'^$', 
        views.show_progress,
        name=u"usetracker_show_progress"),
    url(r'^get_available_hosts/$', 
        views.get_available_hosts,
        name=u"usetracker_get_available_hosts"),
    url(r'^get_available_protocols/$', 
        views.get_available_protocols,
        name=u"usetracker_get_available_protocols"),
    url(r'^get_available_users/$', 
        views.get_available_users,
        name=u"usetracker_get_available_users"),
    url(r'^get_available_fields/$', 
        views.get_available_fields,
        name=u"usetracker_get_available_fields"),
    url(r'^get_filtered_data/$', 
        views.get_filtered_data,
        name=u"usetracker_get_filtered_data"),

]
