# -*- coding: utf-8 -*-
from django.contrib import admin
from usetracker import models

class UseTrackerAdminModel(admin.ModelAdmin):
    list_display = ["protocol", "host", "short_path", "created_at"]
    list_filter = ("protocol", "host", "created_at")
    
admin.site.register(models.UseTracker, UseTrackerAdminModel)
