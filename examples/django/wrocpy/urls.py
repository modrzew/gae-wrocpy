from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'wrocpy.hello.views.home', name='home'),
)
