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

# Global variables
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)
ivle_uri_template_prefix = 'https://ivle.nus.edu.sg/api/Lapi.svc/'

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class StudentProfile(webapp2.RequestHandler):
    # Front page for logged in users
    def get(self):
        user_has_logged_in = users.get_current_user()
        if user_has_logged_in:  # signed in already
            template_values = {
                'student_name': users.get_current_user().nickname(),
                'student_email': users.get_current_user().email(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = jinja_environment.get_template('profile.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)

# add more links like this ,('/wishlist', WishList) inside the square brackets []
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/profile', StudentProfile)],
                              debug=True)