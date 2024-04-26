from rest_framework import serializers
from .models import ProjectInformation,projectAuthority, Deliverable

class ProjectInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectInformation
        fields='__all__'

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deliverable
        fields='__all__'

class ProjectAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model=projectAuthority
        fields='__all__'