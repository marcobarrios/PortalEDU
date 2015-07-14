# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incharges', '0001_initial'),
        ('contact_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InchargeContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_incharge', models.CharField(max_length=45)),
                ('contact_extension_incharge', models.CharField(max_length=10, null=True, blank=True)),
                ('enable_incharge_contact', models.BooleanField(default=1)),
                ('contact_type', models.ForeignKey(to='contact_types.ContactType')),
                ('incharge', models.ForeignKey(to='incharges.Incharge')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
