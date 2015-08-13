# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='benefits',
            new_name='bulk',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='distance',
            new_name='dedicated',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='driver_type',
            new_name='dental',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='endorsements',
            new_name='doubles',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='equipment',
            new_name='flatbed',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hazmat',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='intermodal',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='life',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='med',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='otr',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ownerop',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='regional',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='solo',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='tanker',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='team',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='van',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='vision',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='xtanker',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='miles',
            field=models.TextField(),
        ),
    ]
