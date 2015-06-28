# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id_assignment', models.BigIntegerField(serialize=False, primary_key=True)),
                ('assignment_name', models.CharField(max_length=45)),
                ('enable_assigment', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
