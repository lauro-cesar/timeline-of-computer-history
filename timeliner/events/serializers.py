from rest_framework import serializers
from .models import TimelineEvent
from django.conf import settings



class TimelineEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimelineEvent
		fields = ['label', 'description','eventYear']