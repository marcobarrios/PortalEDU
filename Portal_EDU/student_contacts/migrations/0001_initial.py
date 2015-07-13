# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_student', models.CharField(max_length=45)),
                ('contact_extension_student', models.CharField(max_length=10, null=True, blank=True)),
                ('enable_student_contact', models.BooleanField(default=1)),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
