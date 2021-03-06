#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://writing.quack1.me'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category_%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag_%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing
GOOGLE_ANALYTICS = 'UA-41598568-2'
GOOGLE_ANALYTICS_DOMAIN = 'quack1.me'
DISQUS_SITENAME = 'letswrite'