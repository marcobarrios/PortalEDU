# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('incharge_types', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incharge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name_incharge', models.CharField(max_length=45)),
                ('last_name_incharge', models.CharField(max_length=45)),
                ('birth_date_incharge', models.DateField(max_length=15, blank=True)),
                ('email_incharge', models.EmailField(max_length=254, blank=True)),
                ('home_address_incharge', models.CharField(max_length=80, null=True, blank=True)),
                ('neighborhood_incharge', models.CharField(max_length=50, null=True, blank=True)),
                ('identification_document_incharge', models.CharField(max_length=20)),
                ('profession_incharge', models.CharField(max_length=45, blank=True)),
                ('work_name_incharge', models.CharField(max_length=45, blank=True)),
                ('enable_incharge', models.BooleanField(default=1)),
                ('authentication_incharge', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('genre', models.ForeignKey(to='genres.Genre')),
                ('incharge_type', models.ForeignKey(to='incharge_types.InchargeType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
