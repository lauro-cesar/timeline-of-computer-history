from django.contrib.admin.apps import AdminConfig
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _


class TimeLinerConfig(AdminConfig):
	default_site = 'timeliner.admin.AdminSite'