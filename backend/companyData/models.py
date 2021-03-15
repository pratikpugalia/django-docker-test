from django.db import models


class CompanyData(models.Model):
    company = models.CharField(max_length=500, blank=False, default='')
    month = models.DateTimeField()
    headcount = models.FloatField()
