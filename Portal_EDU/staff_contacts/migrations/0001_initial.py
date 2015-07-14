# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
        ('contact_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_staff', models.CharField(max_length=45)),
                ('contact_extension_staff', models.CharField(max_length=10, null=True, blank=True)),
                ('enable_staff_contact', models.BooleanField(default=1)),
                ('contact_type', models.ForeignKey(to='contact_types.ContactType')),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
