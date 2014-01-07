#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Quack1'
SITENAME = u"Let's Write..."
SITESUBTITLE = u'Some Words About Words'
SITEURL = 'http://writing.quack1.me'
RELATIVE_URLS = True

TIMEZONE = 'Europe/Paris'
THEME = 'storm'
DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category_%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag_%s.atom.xml'
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["upload"]
DISPLAY_PAGES_ON_MENU  = True

# Blogroll
LINKS =  (('Me', 'http://me.quack1.me/'),
					('Mon blog technique', 'https://blog.quack1.me'))

# Social widget
SOCIAL = (('<i class="fa-icon-twitter"></i>', 'https://twitter.com/_Quack1'),
          ('<i class="fa-icon-envelope-alt"></i>', 'mailto:quack+writing@quack1.me'),
	  ('<i class="fa-icon-rss"></i>', FEED_ALL_ATOM))
TWITTER_USERNAME = '_Quack1'