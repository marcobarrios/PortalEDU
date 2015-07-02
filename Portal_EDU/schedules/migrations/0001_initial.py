# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(default=b'Lunes', max_length=15, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Mi\xc3\xa9rcoles', b'Mi\xc3\xa9rcoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'S\xc3\xa1bado', b'S\xc3\xa1bado'), (b'Domingo', b'Domingo')])),
                ('init_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('enable_schedule', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
