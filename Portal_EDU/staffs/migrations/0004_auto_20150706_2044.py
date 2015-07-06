# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_auto_20150706_0458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='authentication',
            new_name='authentication_staff',
        ),
    ]
