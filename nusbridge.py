# Libraries
import urllib2
import json
import webapp2
import jinja2
import os
import datetime
import HTMLParser
from google.appengine.ext import ndb
from urlparse import urlparse
from random import randint

# Global variables
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)
app_domain = 'http://nusbridge.appspot.com/'
ivle_domain = 'https://ivle.nus.edu.sg/'
ivle_api_key = 'O3nIU9c7l8jqYXfBMJlJN'
ivle_token = ''
user_is_validated = False
student_id = ''
student_name = ''
student_email = ''
matriculation_year = ''
first_major = ''
second_major = ''
faculty = ''

class MainPage(webapp2.RequestHandler):
    def get(self):
        global user_is_validated
        
        user_is_validated = False
        template_values = {
            'login_url': ivle_domain + 'api/login/?apikey=' + ivle_api_key + '&url=' + app_domain + 'snapshot'
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Account(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('account.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Profile(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('profile.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Snapshot(webapp2.RequestHandler):
    def get(self):
        global user_is_validated
        global ivle_token
        global student_id
        global student_name
        global student_email
        global matriculation_year
        global first_major
        global second_major
        global faculty

        if user_is_validated == False:
            ivle_token = self.request.get('token')
            user_is_validated = json.load(urllib2.urlopen(ivle_domain + 'api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + ivle_token))['Success']
        
        if user_is_validated:
            student_profile = json.load(urllib2.urlopen(ivle_domain + 'api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + ivle_token))['Results'][0]
            student_id = student_profile['UserID']
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
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('aspirations.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Education(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            modules_taken_obj = json.load(urllib2.urlopen(ivle_domain + 'api/Lapi.svc/Modules_Taken?APIKey=' + ivle_api_key + '&AuthToken=' + ivle_token + '&StudentID=' + student_id))['Results']
            list_of_modules_taken = ''
            number_of_modules_taken = 0
            
            for module in modules_taken_obj:
                if number_of_modules_taken is 0:
                    list_of_modules_taken += module['ModuleCode'] + " " + module['ModuleTitle']
                else:
                    list_of_modules_taken += "," + module['ModuleCode'] + " " + module['ModuleTitle']
                number_of_modules_taken += 1

            template_values = {
                'student_name': student_name,
                'student_email': student_email,
                'list_of_modules_taken': list_of_modules_taken,
                'number_of_modules_taken': number_of_modules_taken
            }
            template = jinja_environment.get_template('education.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Experience(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('experience.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Personality(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('personality.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class SymmetricalConnections(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('symmetrical.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ComplementaryConnections(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('complementary.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ImprovementAdvisory(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            template_values = {
                'student_name': student_name,
                'student_email': student_email
            }
            template = jinja_environment.get_template('improvement.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)
	
class UserName(ndb.Model):
	name=ndb.StringProperty()
	
class UserDisplay(webapp2.RequestHandler):
	#user1=UserName(parent=ndb.Key("NUSBridge",user_name), major="sci")
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
