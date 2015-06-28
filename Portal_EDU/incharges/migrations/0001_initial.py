# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('incharge_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incharge',
            fields=[
                ('id_incharge', models.BigIntegerField(serialize=False, primary_key=True)),
                ('first_name_incharge', models.CharField(max_length=45, blank=True)),
                ('last_name_incharge', models.CharField(max_length=45, blank=True)),
                ('birth_date_incharge', models.CharField(max_length=45, blank=True)),
                ('email_incharge', models.EmailField(max_length=254, blank=True)),
                ('home_address_incharge', models.TextField(null=True, blank=True)),
                ('identification_document_incharge', models.CharField(max_length=20, blank=True)),
                ('profession_incharge', models.CharField(max_length=45, blank=True)),
                ('work_name_incharge', models.CharField(max_length=45, blank=True)),
                ('enable_incharge', models.BooleanField(default=1)),
                ('genre', models.ForeignKey(to='genres.Genre')),
                ('incharge_type', models.ForeignKey(to='incharge_types.InchargeType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
