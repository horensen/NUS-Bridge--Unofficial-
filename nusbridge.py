# Import relevant libraries
import urllib
import webapp2
import jinja2
import os
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from urllib2 import urlopen
from urlparse import urlparse
from random import randint

# Tell this application to look for views inside the templates folder
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())



# add more links like this ,('/wishlist', WishList) inside the square brackets []
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)