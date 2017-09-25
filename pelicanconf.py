# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Service@Tooyum.Com'
SITENAME = u'SDN Hands ON!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('tooyum', 'http://www.tooyum.com/'),)
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file',
         

# Social widget
SOCIAL = (#('You can add links in your config file', '#'),
    #('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PATH="lab"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['org_reader']
ORG_READER_EMACS_LOCATION="/usr/bin/emacs"
#ORG_READER_EMACS_SETTINGS="blog-export.el"
