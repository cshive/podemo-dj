from django.shortcuts import render
from rest_framework import viewsets
from organization.models import Organization
from organization.serializers import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
