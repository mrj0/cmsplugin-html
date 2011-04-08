from django.utils.translation import ugettext as _
from django.db import models

from cms.models import CMSPlugin

class CMSHtmlPlugin(CMSPlugin):
    body = models.TextField(_('body'))

    def __unicode__(self):
        return u'%s' % (self.body,)
