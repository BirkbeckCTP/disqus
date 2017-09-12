from django.template import loader, RequestContext

from plugins.disqus import plugin_settings
from utils import models, setting_handler


def inject_disqus(context):
    request = context.get('request')
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)
    disqus_shortname = setting_handler.get_plugin_setting(plugin, 'disqus_shortname', request.journal)
    disqus_enabled = setting_handler.get_plugin_setting(plugin, 'disqus_enabled', request.journal)

    if not disqus_enabled.value:
        return

    template = loader.get_template('disqus/inject.html')
    disqus_context = {'disqus_shortname': disqus_shortname.processed_value}
    html_content = template.render(disqus_context)

    return html_content
