# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
                ('distance', models.TextField()),
                ('driver_type', models.TextField()),
                ('benefits', models.TextField()),
                ('equipment', models.TextField()),
                ('freight', models.TextField()),
                ('elogs', models.TextField()),
                ('endorsements', models.TextField()),
                ('miles', models.IntegerField()),
                ('pets', models.TextField()),
                ('riders', models.TextField()),
                ('experience', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.ForeignKey(to='truckapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('salary', models.IntegerField()),
                ('distance', models.TextField()),
                ('driver_type', models.TextField()),
                ('benefits', models.TextField()),
                ('equipment', models.TextField()),
                ('freight', models.TextField()),
                ('elogs', models.TextField()),
                ('endorsements', models.TextField()),
                ('miles', models.IntegerField()),
                ('pets', models.TextField()),
                ('riders', models.TextField()),
                ('experience', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
