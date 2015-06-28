from django.db import models

class Incharge(models.Model):
    first_name_incharge = models.CharField(max_length=45, blank=True)
    last_name_incharge = models.CharField(max_length=45, blank=True)
    birth_date_incharge = models.CharField(max_length=45, blank=True)
    email_incharge = models.EmailField(max_length=254, blank=True)
    home_address_incharge = models.TextField(blank=True, null=True)
    identification_document_incharge = models.CharField(max_length=20, blank=True)
    profession_incharge = models.CharField(max_length=45, blank=True)
    work_name_incharge = models.CharField(max_length=45, blank=True)
    enable_incharge = models.BooleanField(default=1)

    incharge_type = models.ForeignKey('incharge_types.InchargeType')
    genre = models.ForeignKey('genres.Genre')

    def __unicode__(self):
        return self.first_name_incharge