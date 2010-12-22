# Django settings for bgcomm project.
import os
#import sys

ROOT_PATH = os.path.dirname(__file__)
#LIB_PATH = os.path.join(ROOT_PATH, 'sct-0.6','communitytools','sphenecoll')
#sys.path.append(ROOT_PATH)
#sys.path.append(LIB_PATH)

try:
    from local_settings import *
except ImportError:
    print u'File local_settings.py is not found. Continuing with production settings.'
DEBUG=False
MAX_POSTS = 5
MAX_EVENTS = 3
SIDEBAR_ADS = 3
DEBUG = True
TEMPLATE_DEBUG = DEBUG
FEEDBACK_EMAILS = ["bulgariancommunity@yahoo.ca","vpandeliev@gmail.com"]
MEMBERSHIP_EMAILS = ["bulgariancommunity@yahoo.ca"]
WEBMASTER_EMAILS = ["vpandeliev@gmail.com",]



ADMINS = (
    ('Velian Pandeliev', 'vpandeliev@gmail.com'),
# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
		'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifyfull,|cut,copy,paste,pastetext,|,undo,redo,|,link,unlink,anchor,image,search,replace,|,bullist,numlist,|,cleanup,help,code,|,insertdate,inserttime,preview",
		'theme_advanced_buttons2' : "",
		'theme_advanced_buttons3': '',
		'theme_advanced_toolbar_location' : "top",
		'theme_advanced_toolbar_align' : "left",
		'theme_advanced_statusbar_location' : "bottom",
		'theme_advanced_resizing' : 'True',
}



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Toronto'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LOCKDOWN_PASSWORDS = ('rodina')

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = 'home/webapps/mediaserv'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = 'http://127.0.0.1:8000/media/'
MEDIA_URL = 'http://bulgarian.webfactional.com/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://bulgarian.webfactional.com/media/admin/'

try:
    from local_settings import MEDIA_ROOT
except ImportError:
    print u'File settings_local.py is not found. Continuing with production settings.'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
#	'sphene.community.groupaware_templateloader.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',


#     'django.template.loaders.eggs.load_template_source',
)



MIDDLEWARE_CLASSES = (
#	'sphene.community.middleware.ThreadLocals',
#	'sphene.community.middleware.GroupMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.middleware.csrf.CsrfResponseMiddleware',
		'django.middleware.doc.XViewMiddleware',
		#'lockdown.middleware.LockdownMiddleware',
	
)

ROOT_URLCONF = 'bgcomm.urls'

TEMPLATE_DIRS = (
	os.path.join(ROOT_PATH, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
		'django.core.context_processors.request',
		'bgcomm.dict.menu_bg',
		'bgcomm.dict.menu_en',
		'bgcomm.dict.menu_fr',
		'bgcomm.views.ad_year_context',
#	'sphene.community.context_processors.navigation',
    
)

#FILEBROWSER_MEDIA_URL = os.path.join(MEDIA_ROOT,'filebrowser')

INSTALLED_APPS = (
    'django.contrib.admin',
	'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
#    'sphene.community',
#    'sphene.sphboard',
#    'sphene.sphwiki',
	'bgcomm.posts',
	#'lockdown',
	'tinymce',
	#'filebrowser',
)


