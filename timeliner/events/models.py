from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings


class TimelineEvent(models.Model):
	isActive = models.BooleanField(default=True)
	dateCreated = models.DateTimeField(auto_now=True,verbose_name=_("Data  de registro"))
	lastModified = models.DateTimeField(auto_now=True,verbose_name=_("Último login"))
	label = models.CharField(max_length=255,blank=True,verbose_name=_("Titulo"))
	description = models.CharField(max_length=255,blank=True,verbose_name=_("Descricao"))
	eventYear =  models.DateField(verbose_name=_("Data do evento"))


	class Meta:
		verbose_name = _("Evento importante")
		verbose_name_plural = _("Eventos importantes")

	def __str__(self):
		return self.label