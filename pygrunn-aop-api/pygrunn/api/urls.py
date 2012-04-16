from django.conf.urls import url, patterns


urlpatterns = patterns('',
    url(r'^(?P<format>\w+)/create_token/?$', 'pygrunn.api.views.create_token'),
    url(r'^(?P<format>\w+)/(?P<function>\w+)/?$', 'pygrunn.api.views.api_call'),
)