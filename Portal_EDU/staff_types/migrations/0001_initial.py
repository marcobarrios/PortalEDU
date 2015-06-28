# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffType',
            fields=[
                ('id_staff_type', models.BigIntegerField(serialize=False, primary_key=True)),
                ('staff_type', models.CharField(max_length=45)),
                ('enable_staff_type', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
