from django.db import models

class Module(models.Model):
    id_module = models.BigIntegerField(primary_key=True)
    module_name = models.CharField(max_length=45)
    enable_module = models.BooleanField(default=1)