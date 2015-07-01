# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planifications', '0001_initial'),
        ('courses', '0002_auto_20150701_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='planifications',
            field=models.ManyToManyField(to='planifications.Planification', null=True, blank=True),
            preserve_default=True,
        ),
    ]
