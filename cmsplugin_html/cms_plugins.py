from django.utils.translation import ugettext as _
from django.template import Template

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.utils import plugin_tags_to_user_html

from cmsplugin_html.models import CMSHtmlPlugin

from django.utils.safestring import mark_safe

class HtmlPlugin(CMSPluginBase):
    model = CMSHtmlPlugin
    name = _('HTML')
    render_template = 'cmsplugin_html/html.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': mark_safe(Template(instance.body).render(context)),
            'object': instance,
            'placeholder': placeholder
        })
        return context
plugin_pool.register_plugin(HtmlPlugin)
