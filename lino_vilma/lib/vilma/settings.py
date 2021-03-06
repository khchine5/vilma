# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Base Django settings for Lino Vilma applications.

"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_vilma import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Vilma"
    version = SETUP_INFO['version']
    url = "http://vilma.lino-framework.org/"

    demo_fixtures = ['std', 'demo', 'demo2', 'checkdata']
                     # 'linotickets',
                     # 'tractickets', 'luc']

    # project_model = 'tickets.Project'
    # project_model = 'deploy.Milestone'
    textfield_format = 'html'
    user_types_module = 'lino_vilma.lib.vilma.user_types'
    workflows_module = 'lino_vilma.lib.vilma.workflows'
    obj2text_template = "**{0}**"

    default_build_method = 'appyodt'
    
    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'
    
    # migration_class = 'lino_vilma.lib.vilma.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_noi"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.extjs'
        # yield 'lino.modlib.bootstrap3'
        # yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        # yield 'lino.modlib.users'
        yield 'lino_vilma.lib.contacts'
        # yield 'lino_xl.lib.online.users'
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.phones'
        yield 'lino_noi.lib.courses'
        # yield 'lino_noi.lib.products'

        yield 'lino_xl.lib.topics'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_noi.lib.tickets'
        yield 'lino_xl.lib.skills'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_noi.lib.working'
        yield 'lino_xl.lib.lists'
        yield 'lino_xl.lib.blogs'

        # yield 'lino.modlib.changes'
        # yield 'lino.modlib.notify'
        # yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino.modlib.export_excel'
        # yield 'lino.modlib.tinymce'
        yield 'lino.modlib.checkdata'
        # yield 'lino.modlib.smtpd'
        yield 'lino.modlib.weasyprint'
        # yield 'lino_xl.lib.appypod'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.comments'
        yield 'lino.modlib.dashboard'

        # yield 'lino.modlib.awesomeuploader'

        # yield 'lino_noi.lib.noi'
        yield 'lino_vilma.lib.vilma'
        # yield 'lino_xl.lib.inbox'
        # yield 'lino_xl.lib.mailbox'
        # yield 'lino_xl.lib.meetings'


    def setup_plugins(self):
        super(Site, self).setup_plugins()
        # self.plugins.comments.configure(
        #     commentable_model='tickets.Ticket')
        # self.plugins.skills.configure(
        #     demander_model='contacts.Person')
        # self.plugins.addresses.configure(
        #     partner_model='contacts.Person')
        # self.plugins.skills.configure(
        #     demander_model='tickets.Ticket')
        # self.plugins.tickets.configure(
        #     site_model='cal.Room',
        #     milestone_model='courses.Course')

    def get_default_required(self, **kw):
        # overrides the default behaviour which would add
        # `auth=True`. In Lino Noi everybody can see everything.
        return kw

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        tb.add_action(self.models.contacts.Persons)
        tb.add_action(self.models.contacts.Companies)
        # tb.add_action(self.modules.deploy.MyMilestones)
        # tb.add_action(self.models.tickets.MyTickets)
        # tb.add_action(self.models.tickets.TicketsToTriage)
        # tb.add_action(self.models.tickets.TicketsToTalk)
        # tb.add_action(self.modules.tickets.TicketsToDo)

        a = self.models.users.MySettings.default_action
        tb.add_instance_action(
            user, action=a, label=_("My settings"))
        # handler = self.action_call(None, a, dict(record_id=user.pk))
        # handler = "function(){%s}" % handler
        # mysettings = dict(text=_("My settings"),
        #                   handler=js_code(handler))
        
    # def get_dashboard_items(self, user):
    #     """Defines the story to be displayed on the admin main page.

    #     """
    #     for i in super(Site, self).get_dashboard_items(user):
    #         yield i
    #     yield self.models.lists.Lists


# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'

