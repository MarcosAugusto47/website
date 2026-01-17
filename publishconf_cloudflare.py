import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Cloudflare Pages deployment (root domain)
SITEURL = "https://website.marcosbsb2014.workers.dev"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feed.xml"
DELETE_OUTPUT_DIRECTORY = True
