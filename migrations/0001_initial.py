# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UseTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(null=True, verbose_name='Created at', blank=True)),
                ('protocol', models.CharField(max_length=50, null=True, verbose_name='Protocol', blank=True)),
                ('host', models.CharField(max_length=200, null=True, verbose_name='Host', blank=True)),
                ('path', models.TextField(null=True, verbose_name='Path', blank=True)),
                ('get_params', models.TextField(null=True, verbose_name='Params (GET)', blank=True)),
                ('headers', models.TextField(null=True, verbose_name='Headers', blank=True)),
                ('post_payload', models.TextField(null=True, verbose_name='Payload (POST)', blank=True)),
                ('username', models.TextField(null=True, verbose_name='Username', blank=True)),
                ('exception', models.TextField(null=True, verbose_name='Exception', blank=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Use tracker',
                'verbose_name_plural': 'Use tracker',
            },
        ),
    ]
