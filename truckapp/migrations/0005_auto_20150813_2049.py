# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckapp', '0004_auto_20150813_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='local',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='none',
            field=models.TextField(null=True, blank=True),
        ),
    ]
