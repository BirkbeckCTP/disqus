from django.db import models

class Settings(models.Model):
	disqus_shortname = models.CharField(max_length=20)
	enabled = models.BooleanField(default=False)