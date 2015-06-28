# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalBackGround',
            fields=[
                ('id_medical_background', models.BigIntegerField(serialize=False, primary_key=True)),
                ('title_medical_background', models.CharField(max_length=45, blank=True)),
                ('description_medical_background', models.TextField()),
                ('enable_medical_background', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
