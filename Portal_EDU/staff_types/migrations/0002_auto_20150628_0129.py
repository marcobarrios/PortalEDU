# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stafftype',
            name='id_staff_type',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
