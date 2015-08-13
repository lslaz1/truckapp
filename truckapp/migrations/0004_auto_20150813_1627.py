# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckapp', '0003_auto_20150812_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='experience',
            field=models.IntegerField(),
        ),
    ]
