# Libraries
import urllib2
import json
import webapp2
import jinja2
import os
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from urlparse import urlparse
from random import randint

# Global variables
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)
app_domain = 'http://nusbridge.appspot.com/'
ivle_domain = 'https://ivle.nus.edu.sg/'
ivle_api_key = 'O3nIU9c7l8jqYXfBMJlJN'
ivle_token = ''
user_is_validated = False
student_name = ''
student_email = ''
matriculation_year = ''
first_major = ''
second_major = ''
faculty = ''

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'login_url': ivle_domain + 'api/login/?apikey=' + ivle_api_key + '&url=' + app_domain + 'snapshot'
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Account(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('account.html')
        self.response.out.write(template.render())

class Profile(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'student_name': users.get_current_user().nickname(),
            'student_email': users.get_current_user().email(),
            'logout': users.create_logout_url(self.request.host_url),
        }
        template = jinja_environment.get_template('profile.html')
        self.response.out.write(template.render(template_values))

class Snapshot(webapp2.RequestHandler):
    def get(self):
        ivle_token = self.request.get('token')
        user_is_validated = json.load(urllib2.urlopen(ivle_domain + 'api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + ivle_token))['Success']
        
        if user_is_validated:
            student_profile = json.load(urllib2.urlopen(ivle_domain + 'api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + ivle_token))['Results'][0]
            student_name = student_profile['Name']
            student_email = student_profile['Email']
            matriculation_year = student_profile['MatriculationYear']
            first_major = student_profile['FirstMajor']
            second_major = student_profile['SecondMajor']
            faculty = student_profile['Faculty']

            template_values = {
                'student_name': student_name,
                'student_email': student_email,
                'matriculation_year': matriculation_year,
                'first_major': first_major,
                'second_major': second_major,
                'faculty': faculty
            }

            template = jinja_environment.get_template('snapshot.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

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
	#user1=UserName(parent=ndb.Key("NUSBridge","User Acc"), name="Mary")
	#user1.put()
	global template
	template = jinja_environment.get_template('testingNdb.html')
	def get(self):
		global template
		self.response.out.write(template.render())
	def post(self):
		global template
		user_name=self.request.get('username')
		if(user_name!=None):
			key=ndb.Key("NUSBridge","User Acc")
			results=UserName.query(UserName.name==user_name).fetch()
			if results:
				for result in results:
					self.response.out.write('<blockquote>%s is a registered user</blockquote>'%(result.name))
			else:
				self.response.out.write('<blockquote>%s is a not a registered user</blockquote>'%(user_name))
		self.response.out.write(template.render())

# Add more links like this ,('/wishlist', WishList) in the square brackets []
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
