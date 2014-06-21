# LIBRARIES
from difflib import SequenceMatcher
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from random import randint
from urlparse import urlparse
from webapp2_extras import sessions
import cgi
import datetime
import HTMLParser
import jinja2
import json
import app_datastore
import os
import urllib
import urllib2
import webapp2





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
    'secret_key': ivle_api_key
}





# INHERITED REQUEST HANDLERS
class MainPage(BaseHandler):
    def get(self):
        self.session['ivle_token'] = ""
        self.session['is_valid'] = False

        template_values = {
            'login_url': 'https://ivle.nus.edu.sg/api/login/?apikey=' + ivle_api_key + '&url=' + app_domain + 'snapshot',
            'number_of_users': app_datastore.get_number_of_users()
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Snapshot(BaseHandler):
    def get(self):
        # Retrieve token
        if self.session.get('is_valid') != True:
            self.session['ivle_token'] = self.request.get('token')
            self.session['is_valid'] = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + self.session.get('ivle_token')))['Success']
        
        # If the user is authenticated and therefore token is not empty
        if self.session.get('is_valid') == True and self.session.get('ivle_token') != '':

            # Retrieve profile information from IVLE and remember for the current browser session
            student_profile_object = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + self.session.get('ivle_token')))['Results'][0]
            self.session['student_id'] = student_profile_object['UserID']
            self.session['student_name'] = student_profile_object['Name']
            self.session['student_email'] = student_profile_object['Email']
            self.session['student_matriculation_year'] = student_profile_object['MatriculationYear']
            self.session['student_first_major'] = student_profile_object['FirstMajor']
            self.session['student_second_major'] = student_profile_object['SecondMajor']
            self.session['student_faculty'] = student_profile_object['Faculty']
            best_modules_html = ''
            aspirations_html = ''

            # If the user exists
            if app_datastore.user_exists(self.session['student_id']):
                # Describe existing aspirations
                try:
                    aspirations = app_datastore.get_aspirations(self.session['student_id']).aspirations
                    number_of_aspirations = len(aspirations)
                    aspiration_id = 1
                    for aspiration in aspirations:
                        if aspiration[0] in "aeiou":
                            aspirations_html += "an "
                        else:
                            aspirations_html += "a "
                        aspirations_html += aspiration
                        if aspiration_id + 1 < number_of_aspirations:
                            aspirations_html += ", "
                        elif aspiration_id + 1 == number_of_aspirations:
                            aspirations_html += " or "
                        aspiration_id += 1
                except IndexError:
                    pass

                # Describe existing best modules
                try:
                    best_modules = app_datastore.get_education(self.session['student_id']).best_modules
                    number_of_best_modules = len(best_modules)
                    max_number_of_modules_to_list = 3
                    if number_of_best_modules > max_number_of_modules_to_list:
                        remaining_best_module_count = number_of_best_modules - max_number_of_modules_to_list
                        best_module_id_1 = randint(0, number_of_best_modules-1)
                        best_module_id_2 = randint(0, number_of_best_modules-1)
                        best_module_id_3 = randint(0, number_of_best_modules-1)
                        best_modules_html = best_modules[best_module_id_1] + ", " + best_modules[best_module_id_2] + ", " + best_modules[best_module_id_3] + " and " + str(remaining_best_module_count) + " other module"
                        if remaining_best_module_count > 1:
                            best_modules_html += "s"
                    else:
                        i = 1
                        for best_module in best_modules:
                            best_modules_html += best_module
                            if i + 1 < number_of_best_modules:
                                best_modules_html += ", "
                            elif i + 1 == number_of_best_modules:
                                best_modules_html += " and "
                            i += 1
                except IndexError:
                    pass

            # else if the user is new
            else:
                # Register into the datastore
                app_datastore.insert_user(student_profile_object)
                
			
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'matriculation_year': self.session.get('student_matriculation_year'),
                'first_major': self.session.get('student_first_major'),
                'second_major': self.session.get('student_second_major'),
                'faculty': self.session.get('student_faculty'),
                'best_modules': best_modules_html,
                'number_of_interests': '__________',
                'number_of_skills': '__________',
                'interests': '__________',
                'skills': '__________',
                'aspirations': aspirations_html,
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
            # Retrieve existing user aspirations
            aspirations_html = ""
            try:
                mylist = app_datastore.get_aspirations(self.session['student_id']).aspirations
                for item in mylist:
                    aspirations_html += "<li>" + item + "</li>"
            except IndexError:
                pass

            # Prepare template values and template
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'existing_aspirations': aspirations_html
            }
            template = jinja_environment.get_template('aspirations.html')

            # Write page
            self.response.out.write(template.render(template_values))
        else:	
            self.redirect(app_domain)

class Education(BaseHandler):
    def post(self):
        # Insert or update aspirations
        aspirations = self.request.get("aspirations").split(",")
        if app_datastore.user_exists(self.session['student_id']):
            app_datastore.insert_or_update_aspirations(self.session['student_id'], aspirations)

        # Redirect to Education questionnaire
        self.redirect(app_domain + "education")

    def get(self):
        if self.session.get('is_valid') == True:
            # Retrieve existing user's best modules
            best_modules_html = ""
            try:
                mylist = app_datastore.get_education(self.session['student_id']).best_modules
                for item in mylist:
                    best_modules_html += "<li>" + item + "</li>"
            except IndexError:
                pass

            # Retrieve all modules completed by the user from IVLE
            urlfetch.set_default_fetch_deadline(10)
            modules_taken_obj = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Modules_Taken?APIKey=' + ivle_api_key + '&AuthToken=' + self.session.get('ivle_token') + '&StudentID=' + self.session['student_id']))['Results']
            list_of_modules_taken = ''
            number_of_modules_taken = 0
            for module in modules_taken_obj:
                if number_of_modules_taken is 0:
                    list_of_modules_taken += module['ModuleCode'] + " " + module['ModuleTitle']
                else:
                    list_of_modules_taken += "," + module['ModuleCode'] + " " + module['ModuleTitle']
                number_of_modules_taken += 1

            # Prepare template values and template
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'list_of_modules_taken': list_of_modules_taken,
                'number_of_modules_taken': number_of_modules_taken,
                'existing_best_modules': best_modules_html
            }
            template = jinja_environment.get_template('education.html')

            # Write page
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Experience(BaseHandler):
    def post(self):
        # Insert or update education
        best_modules = self.request.get("modules").split(",,")
        if app_datastore.user_exists(self.session['student_id']):
            app_datastore.insert_or_update_education(self.session['student_id'], best_modules)

        # Redirect to Experience questionnaire
        self.redirect(app_domain + "experience")

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





# WEB SERVER GATE INTERFACE
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/profile', Profile),
    ('/snapshot', Snapshot),
    ('/aspirations', Aspirations),
    ('/education', Education),
    ('/experience', Experience),
    ('/personality', Personality),
    ('/symmetrical-connections', SymmetricalConnections),
    ('/complementary-connections', ComplementaryConnections),
    ('/improvement-advisory', ImprovementAdvisory)],
    config=config,
    debug=True)