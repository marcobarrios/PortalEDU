# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planification',
            name='id_planification',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
