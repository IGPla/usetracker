# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from usetracker import managers

class UseTracker(models.Model):
    # Relations

    # Fields
    created_at = models.DateTimeField(blank = True,
                                      null = True,
                                      verbose_name = _(u"Created at"))
    finished_at = models.DateTimeField(blank = True,
                                       null = True,
                                       verbose_name = _(u"Finished at"))
    execution_time = models.IntegerField(blank = True,
                                         null = True,
                                         verbose_name = _(u"Execution time"))
    protocol = models.CharField(max_length = 50,
                                blank = True,
                                null = True,
                                verbose_name = _(u"Protocol"))
    host = models.CharField(max_length = 200,
                            blank = True,
                            null = True,
                            verbose_name = _(u"Host"))
    path = models.TextField(blank = True,
                            null = True,
                            verbose_name = _(u"Path"))
    get_params = models.TextField(blank = True,
                                  null = True,
                                  verbose_name = _(u"Params (GET)"))
    headers = models.TextField(blank = True,
                               null = True,
                               verbose_name = _(u"Headers"))
    post_payload = models.TextField(blank = True,
                                    null = True,
                                    verbose_name = _(u"Payload (POST)"))
    username = models.TextField(blank = True,
                                null = True,
                                verbose_name = _(u"Username"))
    exception = models.TextField(blank = True,
                                 null = True,
                                 verbose_name = _(u"Exception"))

    objects = managers.UseTrackerManager()

    # Functions
    def __unicode__(self):
        return unicode(self.pk)

    @property
    def short_path(self):
        try:
            return self.path[0:40]
        except:
            return ""
        
    class Meta:
        ordering = ("-created_at",)
        verbose_name = _(u"Use tracker")
        verbose_name_plural = _(u"Use tracker")

from usetracker.signals import *
