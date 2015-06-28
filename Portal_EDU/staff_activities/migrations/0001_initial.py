# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_staff_activity', models.CharField(max_length=45)),
                ('date_time_staff_activity', models.DateTimeField(null=True, blank=True)),
                ('descripcion_staff_activity', models.CharField(max_length=255, blank=True)),
                ('done_staff_activity', models.IntegerField(null=True, blank=True)),
                ('enable_staff_activity', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
