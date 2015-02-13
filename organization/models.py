from django.db import models

class OrgType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class OrgStatus(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    orgType = models.ForeignKey(OrgType)
    orgStatus = models.ForeignKey(OrgStatus)
    identifier = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phoneNum = models.CharField(max_length=255)
    faxNum = models.CharField(max_length=255)
    ttyNum = models.CharField(max_length=255)
    orgEmail = models.CharField(max_length=255)
    orgUrl = models.CharField(max_length=255)

