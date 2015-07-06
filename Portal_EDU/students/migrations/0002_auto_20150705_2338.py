# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='home_address_student',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='image_student',
            field=models.ImageField(upload_to=b'files/images/students/%Y/%m/%d/', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='neighborhood_student',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
