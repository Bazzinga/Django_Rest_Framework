from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from firstDjango.models import Snippet, EducationInformation, PersonalInformation
from firstDjango.serializers import UserSerializer, GroupSerializer, SnippetSerializer, EducationInformationSerializer, PersonalInformationSerializer

# you cannot change field name queryset and serializer_class


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class EducationInformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer


class PersonalInformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer