from django.conf.urls import url

from plugins.disqus import views

urlpatterns = [
    url(r'^$', views.index, name='disqus_index'),
]