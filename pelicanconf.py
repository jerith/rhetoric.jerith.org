#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeremy Thurgood'
SITENAME = 'jerith dot org'
SITEURL = 'http://localhost:8000'  # Overridden in publishconf.py
SITESUBTITLE = 'Making the world a better place, one line of code at a time.'

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/jerith'),
)

DEFAULT_PAGINATION = 10

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"

# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

THEME = "themes/pelican-elegant"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'summary',
    'sitemap',
    'extract_toc',
    'tipue_search',
]
MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'headerid',
    'toc',
]
DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

SITEMAP = {'format': 'xml'}

RECENT_ARTICLE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100
