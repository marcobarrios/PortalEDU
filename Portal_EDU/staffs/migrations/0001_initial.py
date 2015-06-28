# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('medical_backgrounds', '0001_initial'),
        ('blood_types', '0001_initial'),
        ('staff_activities', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id_staff', models.BigIntegerField(serialize=False, primary_key=True)),
                ('image_staff', models.ImageField(null=True, upload_to=b'staff_images/%Y/%m/%d/', blank=True)),
                ('code_staff', models.CharField(max_length=45, blank=True)),
                ('first_name_staff', models.CharField(max_length=45)),
                ('last_name_staff', models.CharField(max_length=45)),
                ('birth_date_staff', models.CharField(max_length=45, blank=True)),
                ('email_staff', models.EmailField(max_length=254, blank=True)),
                ('home_address_staff', models.TextField(null=True, blank=True)),
                ('identification_document_staff', models.CharField(max_length=20, blank=True)),
                ('nit_staff', models.CharField(max_length=15, blank=True)),
                ('igss_afiliation_number_staff', models.CharField(max_length=25, blank=True)),
                ('teaching_certificate_staff', models.CharField(max_length=45, blank=True)),
                ('title_staff', models.CharField(max_length=45, blank=True)),
                ('cv_file_staff', models.FileField(upload_to=b'staff_cv_files/%Y/%m/%d/', blank=True)),
                ('enable_staff', models.BooleanField(default=1)),
                ('blood_type', models.ForeignKey(to='blood_types.BloodType')),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
                ('genre', models.ForeignKey(to='genres.Genre')),
                ('medical_backgrounds', models.ManyToManyField(to='medical_backgrounds.MedicalBackGround')),
                ('staff_activities', models.ManyToManyField(to='staff_activities.StaffActivity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
