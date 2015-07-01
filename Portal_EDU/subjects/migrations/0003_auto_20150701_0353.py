# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20150701_0347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name_subject',
            new_name='name_csubject',
        ),
    ]
