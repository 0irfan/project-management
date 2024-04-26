from rest_framework import generics
from .models import projectAuthority,ProjectInformation,Deliverable
from .serializer import ProjectInformationSerializer,DeliverableSerializer,ProjectAuthoritySerializer

class ProjectInformationLC(generics.ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectInformationSerializer


class projectInformationRDP(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProjectInformation.objects.all()
    serializer_class=ProjectInformationSerializer



class DeliverableLC(generics.ListCreateAPIView):
    queryset=Deliverable.objects.all()
    serializer_class=DeliverableSerializer


class DeliverableRDP(generics.RetrieveUpdateDestroyAPIView):
    queryset=Deliverable.objects.all()
    serializer_class=DeliverableSerializer


class ProjectAuthorityLC(generics.ListCreateAPIView):
    queryset = projectAuthority.objects.all()
    serializer_class = ProjectAuthoritySerializer


class ProjectAuthorityRDP(generics.RetrieveUpdateDestroyAPIView):
    queryset=projectAuthority.objects.all()
    serializer_class=ProjectAuthoritySerializer
