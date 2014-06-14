# LIBRARIES
import urllib2
import NusDatastore
import json
import webapp2
import jinja2
import os
import datetime
import HTMLParser
import NusDatastore
from google.appengine.ext import ndb
#from appengine_utilities import sessions
from webapp2_extras import sessions
from urlparse import urlparse
from random import randint


# GLOBAL VARIABLES
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"), autoescape=True)
app_domain = 'http://nusbridge.appspot.com/'
ivle_api_key = 'O3nIU9c7l8jqYXfBMJlJN'


# BASE REQUEST HANDLER (SESSION MANAGEMENT)
class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request
        self.session_store = sessions.get_store(request=self.request)
 
        try:
            # Dispatch the request
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions
            self.session_store.save_sessions(self.response)
 
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key
        return self.session_store.get_session()

config = {}

config['webapp2_extras.sessions'] = {
    'secret_key': ivle_api_key,
}


# INHERITED REQUEST HANDLERS
class MainPage(BaseHandler):
    def get(self):
        self.session['ivle_token'] = ""
        self.session['is_valid'] = False
        template_values = {
            'login_url': 'https://ivle.nus.edu.sg/api/login/?apikey=' + ivle_api_key + '&url=' + app_domain + 'snapshot'
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Snapshot(BaseHandler):
    def get(self):
        if self.session.get('is_valid') != True:
            self.session['ivle_token'] = self.request.get('token')
            self.session['is_valid'] = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + self.session.get('ivle_token')))['Success']
        
        if self.session.get('is_valid') == True:
            student_profile_object = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + self.session.get('ivle_token')))['Results'][0]
            self.session['student_id'] = student_profile_object['UserID']
            self.session['student_name'] = student_profile_object['Name']
            self.session['student_email'] = student_profile_object['Email']
            self.session['student_matriculation_year'] = student_profile_object['MatriculationYear']
            self.session['student_first_major'] = student_profile_object['FirstMajor']
            self.session['student_second_major'] = student_profile_object['SecondMajor']
            self.session['student_faculty'] = student_profile_object['Faculty']

            if NusDatastore.userExist(self.session['student_id']) == False:
                NusDatastore.createUser(student_profile_object)
			
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'matriculation_year': self.session.get('student_matriculation_year'),
                'first_major': self.session.get('student_first_major'),
                'second_major': self.session.get('student_second_major'),
                'faculty': self.session.get('student_faculty'),
                'three_or_less_modules': '__________',
                'remaining_module_count': '__________',
                'number_of_interests': '__________',
                'number_of_skills': '__________',
                'interests': '__________',
                'skills': '__________',
                'aspirations': '__________',
                'two_strengths_from_two_traits_at_work': '__________',
                'activities': '__________',
                'two_stengths_from_two_traits_as_a_friend': '__________',
                'two_best_from_two_traits': '__________',
                'advice': '__________',
                'gender': '__________',
                'country': '__________',
                'age': '__________',
                'date_of_birth': '__________',
                'social_networks': '__________',
                'website': '__________',
                'associations': '__________'
            }

            template = jinja_environment.get_template('snapshot.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Aspirations(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'existing_aspirations': ''
            }
            template = jinja_environment.get_template('aspirations.html')
            self.response.out.write(template.render(template_values))
        else:	
            self.redirect(app_domain)

class Education(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            modules_taken_obj = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Modules_Taken?APIKey=' + ivle_api_key + '&AuthToken=' + self.session.get('ivle_token') + '&StudentID=' + self.session['student_id']))['Results']
            list_of_modules_taken = ''
            number_of_modules_taken = 0
            
            for module in modules_taken_obj:
                if number_of_modules_taken is 0:
                    list_of_modules_taken += module['ModuleCode'] + " " + module['ModuleTitle']
                else:
                    list_of_modules_taken += "," + module['ModuleCode'] + " " + module['ModuleTitle']
                number_of_modules_taken += 1

            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'list_of_modules_taken': list_of_modules_taken,
                'number_of_modules_taken': number_of_modules_taken
            }
            template = jinja_environment.get_template('education.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Experience(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('experience.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Personality(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('personality.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class SymmetricalConnections(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('symmetrical.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ComplementaryConnections(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('complementary.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ImprovementAdvisory(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('improvement.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Profile(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email')
            }
            template = jinja_environment.get_template('profile.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)


# FOR TESTING
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


# NDB MODELS
class UserName(ndb.Model):
    name=ndb.StringProperty()


# APP WSGI APPLICATION
app = webapp2.WSGIApplication([('/', MainPage), ('/profile', Profile), ('/snapshot', Snapshot), ('/aspirations', Aspirations), ('/education', Education), ('/experience', Experience), ('/personality', Personality), ('/symmetrical-connections', SymmetricalConnections), ('/complementary-connections', ComplementaryConnections), ('/improvement-advisory', ImprovementAdvisory), ('/testingNdb', UserDisplay)], config=config, debug=True)
