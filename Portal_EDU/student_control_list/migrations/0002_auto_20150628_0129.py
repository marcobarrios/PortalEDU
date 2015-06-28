# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_control_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcontrollist',
            name='id_student_control_list',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
