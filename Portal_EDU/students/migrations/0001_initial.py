# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genres', '0001_initial'),
        ('blood_types', '0001_initial'),
        ('medical_backgrounds', '0001_initial'),
        ('incharges', '0001_initial'),
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_student', models.ImageField(upload_to=b'files/images/students/%Y/%m/%d/', blank=True)),
                ('code_student', models.CharField(max_length=45, blank=True)),
                ('first_name_student', models.CharField(max_length=45)),
                ('last_name_student', models.CharField(max_length=45)),
                ('birth_date_student', models.DateField(max_length=15)),
                ('email_student', models.EmailField(max_length=254, blank=True)),
                ('home_address_student', models.CharField(max_length=80, null=True, blank=True)),
                ('neighborhood_student', models.CharField(max_length=50, null=True, blank=True)),
                ('enable_student', models.BooleanField(default=1)),
                ('authentication_student', models.OneToOneField(related_name=b'student', to=settings.AUTH_USER_MODEL)),
                ('blood_type', models.ForeignKey(to='blood_types.BloodType')),
                ('genre', models.ForeignKey(to='genres.Genre')),
                ('grade', models.ForeignKey(blank=True, to='grades.Grade', null=True)),
                ('incharges', models.ManyToManyField(to='incharges.Incharge')),
                ('medical_backgrounds', models.ManyToManyField(to='medical_backgrounds.MedicalBackGround', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
