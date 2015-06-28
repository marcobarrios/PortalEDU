# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_csubject', models.CharField(max_length=45, blank=True)),
                ('min_note_subject', models.DecimalField(default=60.0, max_digits=5, decimal_places=2)),
                ('max_note_subject', models.DecimalField(default=100.0, max_digits=5, decimal_places=2)),
                ('enable_subject', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
