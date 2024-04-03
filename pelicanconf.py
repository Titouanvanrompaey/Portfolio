AUTHOR = 'Equipe CPI'
SITENAME = 'Portfolio'
SITEURL = ''

PATH = 'content'


TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Thème du site :
THEME = 'materialistic-pelican'

# Options ajoutées :
#DEFAULT_CATEGORY = 'test'
DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = True
STATIC_CHECK_IF_MODIFIED = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
SUMMARY_MAX_LENGTH = 100000000000
OUTPUT_PATH= 'docs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_CDN = True
PRIMARY_COLOR = 'indigo'
ACCENT_COLOR = 'light blue'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True