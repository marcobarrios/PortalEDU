# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_assistance', models.CharField(max_length=45, null=True, blank=True)),
                ('date_assistance', models.DateField()),
                ('course', models.ForeignKey(to='courses.Course')),
                ('students', models.ManyToManyField(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
