from django.contrib import admin
from organization.models import OrgStatus, OrgType, Organization

admin.site.register(Organization)
admin.site.register(OrgStatus)
admin.site.register(OrgType)
# Register your models here.
