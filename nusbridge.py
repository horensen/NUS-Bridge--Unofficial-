# Libraries
import urllib2
import NusDatastore
import json
import webapp2
import jinja2
import os
import datetime
import HTMLParser
#import nus_datastore
from google.appengine.ext import ndb
from urlparse import urlparse
from random import randint

# Global variables
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)
app_domain = 'http://nusbridge.appspot.com/'
ivle_api_key = 'O3nIU9c7l8jqYXfBMJlJN'



class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'login_url': 'https://ivle.nus.edu.sg/api/login/?apikey=' + ivle_api_key + '&url=' + app_domain + 'snapshot'
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

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
    user_is_validated=False
    ivle_token = ''
    student_id = ''
    student_name = ''
    student_email = ''
    matriculation_year = ''
    first_major = ''
    second_major = ''
    faculty = ''

    def get(self):
        if self.user_is_validated==False:
            self.ivle_token = self.request.get('token')
            self.user_is_validated = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + self.ivle_token))['Success']
        
        if self.user_is_validated:
            self.student_profile = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + self.ivle_token))['Results'][0]
            
            self.student_id = self.student_profile['UserID']
            self.student_name = self.student_profile['Name']
            self.student_email = self.student_profile['Email']
            self.matriculation_year = self.student_profile['MatriculationYear']
            self.first_major = self.student_profile['FirstMajor']
            self.second_major = self.student_profile['SecondMajor']
            self.faculty = self.student_profile['Faculty']

            if NusDatastore.userExist(self.student_id):
                pass
            else:
                NusDatastore.createUser(self.student_profile, str(self.user_is_validated), self.ivle_token)
			
            template_values = {
                'student_name': self.student_name,
                'student_email': self.student_email,
                'matriculation_year': self.matriculation_year,
                'first_major': self.first_major,
                'second_major': self.second_major,
                'faculty': self.faculty
            }

            template = jinja_environment.get_template('snapshot.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Aspirations(webapp2.RequestHandler):
    def get(self):
        self.student_name = NusDatastore.retrieveUserName()
        self.student_email= Snapshot.student_email
        if user_is_validated:
            template_values = {
                'student_name': self.student_name,
                'student_email': self.student_email
            }
            template = jinja_environment.get_template('aspirations.html')
            self.response.out.write(template.render(template_values))
        else:
            pass		
            self.redirect(app_domain)

class Education(webapp2.RequestHandler):
    def get(self):
        global student_name
        global student_email

        if user_is_validated:
            modules_taken_obj = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Modules_Taken?APIKey=' + ivle_api_key + '&AuthToken=' + ivle_token + '&StudentID=' + student_id))['Results']
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
