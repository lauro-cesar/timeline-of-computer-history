from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import TimelineEvent
from django.utils.encoding import smart_str,smart_text
import base64



@receiver(pre_save, sender=TimelineEvent)
def timeline_event(sender, instance=None, created=False, **kwargs):
	pass


