from django import forms

from plugins.disqus import models

class DisqusAdminForm(forms.Form):

    disqus_shortname = forms.CharField()
    disqus_enabled = forms.BooleanField(required=False)