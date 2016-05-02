PLUGIN_NAME = 'Disqus Plugin'
DESCRIPTION = 'This plugin injects disqus into the footer of the article.'
AUTHOR = 'Andy Byers'
VERSION = '1.0'
SHORT_NAME = 'disqus'

from utils import models

def install():
	new_plugin, created = models.Plugin.objects.get_or_create(name=SHORT_NAME, version=VERSION, enabled=True)

	if created:
		print 'Plugin {0} installed.'.format(PLUGIN_NAME)
	else:
		print 'Plugin {0} is already installed.'.format(PLUGIN_NAME)


def hook_registry():
	# On site load, the load function is run for each installed plugin to generate
	# a list of hooks.
	return {'article_footer_block': {'module': 'plugins.disqus.hooks', 'function': 'inject_disqus'}}