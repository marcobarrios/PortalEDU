# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_auto_20150706_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='auth',
            new_name='authentication',
        ),
    ]
