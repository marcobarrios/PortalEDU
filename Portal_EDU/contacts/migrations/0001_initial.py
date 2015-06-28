# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_contact', models.BigIntegerField(serialize=False, primary_key=True)),
                ('phone_contact', models.CharField(max_length=20)),
                ('enable_contact', models.BooleanField(default=1)),
                ('contact_type', models.ForeignKey(to='contact_types.ContactType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
