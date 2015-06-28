# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id_level', models.BigIntegerField(serialize=False, primary_key=True)),
                ('level_name', models.CharField(max_length=45)),
                ('enable_levels', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
