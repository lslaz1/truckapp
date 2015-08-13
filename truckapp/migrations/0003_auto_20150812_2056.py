# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckapp', '0002_auto_20150812_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bulk',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dedicated',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dental',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='doubles',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='elogs',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='experience',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='flatbed',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='freight',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hazmat',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='intermodal',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='life',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='med',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='miles',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='otr',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ownerop',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pets',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='regional',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='riders',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='salary',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='solo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tanker',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='team',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='van',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='vision',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='xtanker',
            field=models.TextField(null=True, blank=True),
        ),
    ]
