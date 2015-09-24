# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usetracker', '0002_usetracker_finished_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='usetracker',
            name='execution_time',
            field=models.IntegerField(null=True, verbose_name='Execution time', blank=True),
        ),
    ]
