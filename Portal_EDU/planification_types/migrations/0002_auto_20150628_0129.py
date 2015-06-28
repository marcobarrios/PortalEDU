# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planification_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planificationtype',
            name='id_planification_type',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
