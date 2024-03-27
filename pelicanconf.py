AUTHOR = 'Van Rompaey'
SITENAME = 'Portfolio'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'
THEME = './materialistic-pelican'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
OUTPUT_PATH= 'docs'
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget

SOCIAL = (('Github', 'https://github.com/eswarm'),
		  ('Google plus', 'https://plus.google.com/102630360601349400454/about'),
          ('Twitter', 'https://twitter.com/eswar_001'))

DEFAULT_PAGINATION = 4

PRIMARY_COLOR = 'Indigo'
ACCENT_COLOR = 'Light Blue'
GOOGLE_PLUS_COMMENTS = True
USE_CDN = True


STATIC_PATHS = ['images']

# provide an absolute url here, for pages to work properly.
USER_LOGO_URL = SITEURL + '/images/logo.png'
# provide an absolute url here, for pages to work properly.
USER_AVATAR_URL = SITEURL + '/images/avatar.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True