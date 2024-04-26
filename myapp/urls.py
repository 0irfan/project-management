from django.urls import path
from .views import ProjectInformationLC,projectInformationRDP,DeliverableLC,DeliverableRDP,ProjectAuthorityLC,ProjectAuthorityRDP



urlpatterns = [

    path('Project/', ProjectInformationLC.as_view()),

    path('Project/<int:pk>/',projectInformationRDP.as_view()),

    path('Deliverable/',DeliverableLC.as_view()),

    path('Deliverable/<int:pk>/',DeliverableRDP.as_view()),

    path('ProjectAuthority/', ProjectAuthorityLC.as_view()),

    path('ProjectAuthority/<int:pk>/', ProjectAuthorityRDP.as_view()),

]