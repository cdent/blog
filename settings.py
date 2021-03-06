
SITENAME = "Sileht's Blog"
SITEURL = "https://blog.sileht.net"
AUTHOR = "Mehdi Abaakouk"
TIMEZONE = "Europe/Paris"

SOCIAL = (
    ('twitter', 'http://twitter.com/sileht'),
    ('github', 'http://github.com/sileht'),
    ('linkedin', 'http://fr.linkedin.com/pub/mehdi-abaakouk/24/9b0/27/'),
    ('sileht on IRC', ''),
    ('launchpad', 'https://launchpad.net/~sileht'),
    ('email', 'mailto:sileht@sileht.net'),
)

# STYLE
THEME = "/var/www/blog.sileht.net/pelican-twitchy"
SUMMARY_MAX_LENGTH = 150
RECENT_POST_COUNT = 10
BOOTSTRAP_THEME = "sandstone"
PYGMENTS_STYLE = "tango"
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = True

TYPOGRIFY = True
MARKUP = ('rst', 'md', 'mkd')

# PLUGINS
PLUGIN_PATHS = ['/var/www/blog.sileht.net/pelican-plugins']
PLUGINS = [
    'better_code_samples',
    'better_figures_and_images',
]
RESPONSIVE_IMAGES = True  # better_figures_and_images

# SETUP
LOAD_CONTENT_CACHE = False
OUTPUT_PATH = "/var/www/blog.sileht.net/output/dev"
DELETE_OUTPUT_DIRECTORY = True
