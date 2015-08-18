# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckapp', '0005_auto_20150813_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
    ]
