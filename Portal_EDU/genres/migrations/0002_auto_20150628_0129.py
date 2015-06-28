# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='id_genre',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
