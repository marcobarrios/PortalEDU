# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_genre', models.BigIntegerField(serialize=False, primary_key=True)),
                ('genre', models.CharField(max_length=20)),
                ('enable_genre', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
