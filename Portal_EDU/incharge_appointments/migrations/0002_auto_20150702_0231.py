# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incharge_appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inchargeappointment',
            name='duration_incharge_appointment',
            field=models.PositiveIntegerField(help_text=b'En minutos', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inchargeappointment',
            name='subject_incharge_appointment',
            field=models.CharField(max_length=45),
        ),
    ]
