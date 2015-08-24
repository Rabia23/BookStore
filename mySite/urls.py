from django.conf.urls import include, url
from views import index
from django.contrib import admin

urlpatterns = [
    url(r'^$', index),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]