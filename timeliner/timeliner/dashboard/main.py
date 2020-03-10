"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'backend.maindashbard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'backend.maindashbard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class MainDashboard(Dashboard):
    """
    Custom index dashboard for backend.
    """
    columns = 2
    title = ''
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
                title=_('Usuários e grupos'),
                models=['django.contrib.auth.*','accounts.models.*',]
            ))

        self.children.append(modules.ModelList(
                title=_('Frontend'),
                models=['django.contrib.sites.*','django.contrib.flatpages.*']
            ))

        # self.children.append(modules.ModelList(
        #         title=_('Efa Serviços '),
        #         models=['accounts.models.*',]
        #     ))

        # self.children.append(modules.ModelList(
        #         title=_('Efa Produtos'),
        #         models=['accounts.models.*',]
        #     ))

        # self.children.append(modules.ModelList(
        #         title=_('Serviços no App'),
        #         models=['efaservices.models.*',]
        #     ))



        self.children.append(modules.LinkList(
            _('Support'),
            draggable=True,
            deletable=True,
            collapsible=True,
            children=[
                {
                    'title': _('Página do desenvolvedor'),
                    'url': 'https://www.linkedin.com/in/lauro-cesar/',
                    'external': True,
                    'attrs': {'target': '_blank'},
                },
                {
                    'title': _('lauro@hostcert.com.br'),
                    'url': 'mailto://lauro@hostcert.com.br',
                    'external': True,
                    'attrs': {'target': '_blank'},
                }
            ]
        ))


        # self.children.append(modules.RecentActions(_('Recent Actions'),limit=5))



class MainAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for backend.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)
        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(MainAppIndexDashboard, self).init_with_context(context)
