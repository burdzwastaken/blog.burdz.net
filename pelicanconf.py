#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Matt Burdan'
SITEURL = 'http://localhost:8000'
SITENAME = "Matt Burdan's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'infosec/DFIR/DevOps/containers(everywhere!)/nerd'
SITEDESCRIPTION = '%s\'s Thoughts' % AUTHOR
SITELOGO = 'https://www.gravatar.com/avatar/82c34353ff545bf6a6b1098926cd6421?s=120'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = './Flex'
PATH = 'content'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('Resume', 'https://github.com/burdzwastaken/resume/blob/master/README.md'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/burdz'),
          ('github', 'https://github.com/burdzwastaken'),
          ('twitter', 'https://twitter.com/burdzwastaken'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True
