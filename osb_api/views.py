from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from showcase.models import Storyboard, Storyboarder
from django.contrib.auth.models import User
from osb_api.serializers import StoryboardSerializer

class StoryboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Storyboard.objects.exclude(approved__exact=False)
    serializer_class = StoryboardSerializer