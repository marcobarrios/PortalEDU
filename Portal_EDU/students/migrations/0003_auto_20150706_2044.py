# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_authentication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='authentication',
            new_name='authentication_student',
        ),
    ]
