# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usetracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usetracker',
            name='finished_at',
            field=models.DateTimeField(null=True, verbose_name='Finished at', blank=True),
        ),
    ]
