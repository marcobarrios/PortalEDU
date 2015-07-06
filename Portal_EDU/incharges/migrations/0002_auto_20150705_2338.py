# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incharges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incharge',
            name='neighborhood_incharge',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incharge',
            name='home_address_incharge',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='identification_document_incharge',
            field=models.CharField(max_length=20),
        ),
    ]
