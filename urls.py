from django.conf.urls.defaults import *
from django.conf import settings
from bgcomm.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
defaultdict = { 'groupName': 'example' }

urlpatterns = patterns('',
#	(r'^admin/filebrowser/', include('filebrowser.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

	('^$', index),
	#('^$', welcome2),
	(r'^(\w{2})$', home_page),
	(r'^(?P<lg>\w{2})/links$', list_of_links),
	(r'^(?P<lg>\w{2})/posts/(?P<pid>[0-9]*)$', single_post),
	(r'^(?P<lg>\w{2})/thanks/(?P<method>\w{1})$', membership_thanks_page),
	(r'^(?P<lg>\w{2})/thanks$', contact_thanks_page),
	(r'^(?P<lg>\w{2})/send_message$', send_message),
	(r'^(?P<lg>\w{2})/membership_request$', membership_request),
	(r'^(?P<lg>\w{2})/archive/(?P<year>[0-9]*)$', single_year_archive),
	(r'^(?P<lg>\w{2})/events$', list_of_events),
	(r'^(?P<lg>\w{2})/about$', about_page),
	(r'^(?P<lg>\w{2})/ads/(?P<pid>[0-9]*)$', single_ad),
	(r'^(?P<lg>\w{2})/ads$', list_of_ads),
	(r'^(?P<lg>\w{2})/events/(?P<pid>[0-9]*)$', single_event),
	(r'^(?P<lg>\w{2})/(?P<page>[a-z0-9]*)$', static_page),
	

    # Example:
    # (r'^bgcomm/', include('bgcomm.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
