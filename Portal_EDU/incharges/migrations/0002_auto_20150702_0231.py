# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incharges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incharge',
            name='birth_date_incharge',
            field=models.DateField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='first_name_incharge',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='last_name_incharge',
            field=models.CharField(max_length=45),
        ),
    ]
