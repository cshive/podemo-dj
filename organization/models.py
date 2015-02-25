from django.db import models

class OrgType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class OrgStatus(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class Organization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    orgType = models.ForeignKey(OrgType, blank=True, null=True)
    orgStatus = models.ForeignKey(OrgStatus, blank=True, null=True)
    identifier = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postalCode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phoneNum = models.CharField(max_length=255, blank=True, null=True)
    faxNum = models.CharField(max_length=255, blank=True, null=True)
    ttyNum = models.CharField(max_length=255, blank=True, null=True)
    orgEmail = models.CharField(max_length=255, blank=True, null=True)
    orgUrl = models.CharField(max_length=255, blank=True, null=True)

