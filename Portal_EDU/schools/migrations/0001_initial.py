# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_school', models.CharField(max_length=45)),
                ('phone_school', models.CharField(max_length=45, blank=True)),
                ('address_school', models.CharField(max_length=45, blank=True)),
                ('director_name_school', models.CharField(max_length=45, blank=True)),
                ('vission_school', models.TextField(null=True, blank=True)),
                ('mission_school', models.TextField(null=True, blank=True)),
                ('enable_school', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
