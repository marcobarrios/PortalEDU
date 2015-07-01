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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_medical_background', models.CharField(max_length=45)),
                ('description_medical_background', models.TextField(null=True, blank=True)),
                ('treatment_medical_background', models.TextField(null=True, blank=True)),
                ('enable_medical_background', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
