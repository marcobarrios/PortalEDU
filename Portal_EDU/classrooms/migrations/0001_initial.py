# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id_classroom', models.BigIntegerField(serialize=False, primary_key=True)),
                ('classroom', models.CharField(max_length=10)),
                ('enable_classroom', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
