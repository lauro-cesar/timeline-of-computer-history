from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import TimelineEvent
from .serializers import TimelineEventSerializer


from .permissions import IsOwnerOrReadOnly

from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import filters

from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




def TimeLineHome(request):
	template = loader.get_template('events/home.html')
	events = TimelineEvent.objects.filter(isActive=True)
	context = {
			'events':events
	}
	return HttpResponse(template.render(context, request))


class TimelineEventViewSet(viewsets.ModelViewSet):
	serializer_class = TimelineEventSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	authentication_classes = [SessionAuthentication,TokenAuthentication]

	def get_queryset(self):
		return TimelineEvent.objects.filter(isActive=True)
