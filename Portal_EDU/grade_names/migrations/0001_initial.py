# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeName',
            fields=[
                ('id_grade_name', models.BigIntegerField(serialize=False, primary_key=True)),
                ('gradename', models.CharField(max_length=45)),
                ('enable_grade_name', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
