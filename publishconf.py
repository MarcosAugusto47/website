import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://marcosaugusto.com"  # Update with your domain
RELATIVE_URLS = False
FEED_ALL_ATOM = "feed.xml"
DELETE_OUTPUT_DIRECTORY = True
