# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_show_progress_perm(apps, schema_editor):
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")
    UseTracker = apps.get_model("usetracker", "UseTracker")
    content_type = ContentType.objects.get_for_model(UseTracker)
    permission = Permission.objects.create(codename='use_tracker_admin',
                                       name='Use Tracker Admin',
                                       content_type=content_type)

class Migration(migrations.Migration):

    dependencies = [
        ('usetracker', '0003_usetracker_execution_time'),
    ]

    operations = [
        migrations.RunPython(add_show_progress_perm)
    ]
