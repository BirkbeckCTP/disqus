from django.template import loader, RequestContext

from plugins.disqus import plugin_settings
from utils import models
from utils.plugins import setting_handler

def inject_disqus(request):
	plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)
	disqus_shortname = setting_handler.get_setting(plugin, 'disqus_shortname')
	disqus_enabled = setting_handler.get_setting(plugin, 'disqus_enabled')

	if not disqus_enabled:
		return

	template = loader.get_template('disqus/inject.html')
	context = RequestContext(request)
	context.push({'disqus_shortname': disqus_shortname})
	html_content = template.render(context)

	return html_content




