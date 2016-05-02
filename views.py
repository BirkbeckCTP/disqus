from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from plugins.disqus import forms
from plugins.disqus import plugin_settings

from utils.plugins import setting_handler
from utils import models

def index(request):

	plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)
	disqus_shortname = setting_handler.get_setting(plugin, 'disqus_shortname')
	disqus_enabled = setting_handler.get_setting(plugin, 'disqus_enabled')
	admin_form = forms.DisqusAdminForm(initial={'disqus_shortname': disqus_shortname, 'disqus_enabled': disqus_enabled})

	if request.POST:
		admin_form = forms.DisqusAdminForm(request.POST)

		if admin_form.is_valid():
			for setting_name, setting_value in admin_form.cleaned_data.iteritems():
				setting, response = setting_handler.save_setting(plugin, setting_name, setting_value)

				if response:
					messages.add_message(request, messages.SUCCESS, '{0} setting created.'.format(setting_name))
				else:
					messages.add_message(request, messages.SUCCESS, '{0} setting updated.'.format(setting_name))

			return redirect(reverse('disqus_index'))

	template = "disqus/index.html"
	context = {
		'admin_form': admin_form,
	}

	return render(request, template, context)
