# -*- encoding: utf-8 -*-
from django.db import models

class Incharge(models.Model):
    first_name_incharge = models.CharField(max_length=45)
    last_name_incharge = models.CharField(max_length=45)
    birth_date_incharge = models.DateField(max_length=15, blank=True)
    email_incharge = models.EmailField(max_length=254, blank=True)
    home_address_incharge = models.CharField(max_length=80, blank=True, null=True)
    neighborhood_incharge = models.CharField(max_length=50, blank=True, null=True)
    identification_document_incharge = models.CharField(max_length=20)
    profession_incharge = models.CharField(max_length=45, blank=True)
    work_name_incharge = models.CharField(max_length=45, blank=True)
    enable_incharge = models.BooleanField(default=1)

    incharge_type = models.ForeignKey('incharge_types.InchargeType')
    genre = models.ForeignKey('genres.Genre')

    def __str__(self):
        return self.last_name_incharge + ", " + self.first_name_incharge