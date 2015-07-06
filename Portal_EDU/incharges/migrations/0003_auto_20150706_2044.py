# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incharges', '0002_incharge_authentication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incharge',
            old_name='authentication',
            new_name='authentication_incharge',
        ),
    ]
