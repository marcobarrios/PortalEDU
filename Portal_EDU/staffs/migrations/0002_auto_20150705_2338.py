# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='title_staff',
            new_name='profession_staff',
        ),
        migrations.AlterField(
            model_name='staff',
            name='cv_file_staff',
            field=models.FileField(upload_to=b'files/staff_cvn/%Y/%m/%d/', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='home_address_staff',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image_staff',
            field=models.ImageField(null=True, upload_to=b'files/images/staffs/%Y/%m/%d/', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='neighborhood_staff',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
