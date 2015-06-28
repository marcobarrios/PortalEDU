# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id_section', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name_section', models.CharField(max_length=10)),
                ('enable_section', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
