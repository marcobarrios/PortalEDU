# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InchargeType',
            fields=[
                ('id_incharge_type', models.BigIntegerField(serialize=False, primary_key=True)),
                ('incharge_type', models.CharField(max_length=45)),
                ('enable_incharge_type', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
