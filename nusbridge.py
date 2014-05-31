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

class Account(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('account.html')
        self.response.out.write(template.render())

class Profile(webapp2.RequestHandler):
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

class Snapshot(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('snapshot.html')
        self.response.out.write(template.render())

class Aspirations(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aspirations.html')
        self.response.out.write(template.render())

class Education(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('education.html')
        self.response.out.write(template.render())

class Experience(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('experience.html')
        self.response.out.write(template.render())

class Personality(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('personality.html')
        self.response.out.write(template.render())

class SymmetricalConnections(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('symmetrical.html')
        self.response.out.write(template.render())

class ComplementaryConnections(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('complementary.html')
        self.response.out.write(template.render())

class ImprovementAdvisory(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('improvement.html')
        self.response.out.write(template.render())

class UserName(ndb.Model):
	name=ndb.StringProperty()
	
class UserDisplay(webapp2.RequestHandler):
	"""user1=UserName(name="Peter")
	user1.put()
	user2=UserName(name="John")
	user2.put()
	user3=UserName(name="Sandy")
	user3.put()"""
	
	def get(self):
		template = jinja_environment.get_template('testingNdb.html')
		self.response.out.write(template.render())
	def post(self):
		user_name=self.request.get('username')
		if(user_name!=None):
			result=UserName.query(name=user_name).fetch()
			if result:
				self.response.out.write('%s is a registered user'%(result))
			else:
				self.response.out.write('%s is a not a registered user'%(result))
		else:
			self.response.out.write('No input is detected.')

# add more links like this ,('/wishlist', WishList) inside the square brackets []
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/account', Account),
                               ('/profile', Profile),
                               ('/snapshot', Snapshot),
                               ('/aspirations', Aspirations),
                               ('/education', Education),
                               ('/experience', Experience),
                               ('/personality', Personality),
                               ('/symmetrical-connections', SymmetricalConnections),
                               ('/complementary-connections', ComplementaryConnections),
                               ('/improvement-advisory', ImprovementAdvisory),
							                 ('/testingNdb', UserDisplay)],
                              debug=True)