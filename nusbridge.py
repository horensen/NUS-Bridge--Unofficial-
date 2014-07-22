# LIBRARIES
from google.appengine.api import urlfetch
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
from random import randint
from urlparse import urlparse
from webapp2_extras import sessions
import analysis
import app_datastore
import cgi
import datetime
import difflib
import HTMLParser
import four_temperaments
import jinja2
import json
import logging
import os
import random
import string
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
    'secret_key': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
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
    def post(self):
        # Insert or update personality
        words = self.request.get("personality_words").split(",")
        if app_datastore.user_exists(self.session['student_id']):
            app_datastore.insert_or_update_personality(self.session['student_id'], words)

        # Redirect to Snapshot
        self.redirect(app_domain + "snapshot")

    def get(self):
        urlfetch.set_default_fetch_deadline(10)

        # Retrieve token
        if self.session.get('is_valid') != True:
            self.session['ivle_token'] = self.request.get('token')
            self.session['is_valid'] = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Validate?APIKey=' + ivle_api_key + '&Token=' + self.session.get('ivle_token')))['Success']
        
        # If the user is authenticated and token is not empty
        if self.session.get('is_valid') == True and self.session.get('ivle_token') != '':

            # Initialise values
            aspirations_completed = False
            education_completed = False
            experience_completed = False
            personality_completed = False
            aspirations_html = ''
            best_modules_html = ''
            interests_html = ''
            skills_and_knowledge_html = ''
            strengths_at_work_html = ''
            involvements_html = ''
            emotions_html = ''
            strengths_as_a_friend_html = ''
            personality_best_html = ''
            advice_html = ''
            social_networks_html=''

            # If the user's session is new
            if app_datastore.user_exists(self.session.get('student_id')) == False:

                # Retrieve profile information from IVLE and remember for the current browser session
                student_profile_object = json.load(urllib2.urlopen('https://ivle.nus.edu.sg/api/Lapi.svc/Profile_View?APIKey=' + ivle_api_key + '&AuthToken=' + self.session.get('ivle_token')))['Results'][0]
                self.session['student_id'] = student_profile_object['UserID']
                self.session['student_name'] = student_profile_object['Name']
                self.session['student_email'] = student_profile_object['Email']
                self.session['student_matriculation_year'] = student_profile_object['MatriculationYear']
                self.session['student_first_major'] = student_profile_object['FirstMajor']
                self.session['student_second_major'] = student_profile_object['SecondMajor']
                self.session['student_faculty'] = student_profile_object['Faculty']
                self.session['log_identity'] = self.session.get('student_name') + " (" + self.session.get('student_id') + ")" 

                logging.debug(self.session.get('log_identity') + " has logged in")

            # If the user exists in the datastore
            if app_datastore.user_exists(self.session['student_id']):

                # Update the email session variable if there is a different email in the datastore than in IVLE
                if (app_datastore.get_user(self.session['student_id']).email != self.session['student_email']):
                    self.session['student_email'] = app_datastore.get_user(self.session['student_id']).email

                # Describe existing aspirations
                try:
                    aspirations = app_datastore.get_aspirations(self.session['student_id']).aspirations
                    aspirations_completed = app_datastore.get_aspirations(self.session['student_id']).completed
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
                except Exception:
                    pass

                # Describe existing best modules
                try:
                    best_modules = app_datastore.get_education(self.session['student_id']).best_modules
                    education_completed = app_datastore.get_education(self.session['student_id']).completed
                    number_of_best_modules = len(best_modules)
                    if number_of_best_modules > 3:
                        remaining_best_module_count = number_of_best_modules - 3
                        best_module_id_1 = randint(0, number_of_best_modules-1)
                        best_module_id_2 = best_module_id_1
                        while (best_module_id_2 == best_module_id_1):
                            best_module_id_2 = randint(0, number_of_best_modules-1)
                        best_module_id_3 = best_module_id_1
                        while (best_module_id_3 == best_module_id_1 or best_module_id_3 == best_module_id_2):
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
                except Exception:
                    pass

                # Describe existing interests
                try:
                    interests = app_datastore.get_experience(self.session['student_id']).interests
                    experience_completed = app_datastore.get_experience(self.session['student_id']).completed
                    if len(interests) > 3:
                        remaining_interest_count = len(interests) - 3
                        interest_id_1 = randint(0, len(interests)-1)
                        interest_id_2 = interest_id_1
                        while (interest_id_2 == interest_id_1):
                            interest_id_2 = randint(0, len(interests)-1)
                        interest_id_3 = interest_id_1
                        while (interest_id_3 == interest_id_1 or interest_id_3 == interest_id_2):
                            interest_id_3 = randint(0, len(interests)-1)
                        interests_html = interests[interest_id_1] + ", " + interests[interest_id_2] + ", " + interests[interest_id_3] + " and " + str(remaining_interest_count) + " other interest"
                        if remaining_interest_count > 1:
                            interests_html += "s"
                    else:
                        i = 1
                        for interest in interests:
                            interests_html += interest
                            if i + 1 < len(interests):
                                interests_html += ", "
                            elif i + 1 == len(interests):
                                interests_html += " and "
                            i += 1
                except Exception:
                    pass


                # Describe existing skills
                try:
                    sk = app_datastore.get_experience(self.session['student_id']).skills_and_knowledge
                    experience_completed = app_datastore.get_experience(self.session['student_id']).completed
                    if len(sk) > 3:
                        remaining_sk_count = len(sk) - 3
                        sk_id_1 = randint(0, len(sk)-1)
                        sk_id_2 = sk_id_1
                        while (sk_id_2 == sk_id_1):
                            sk_id_2 = randint(0, len(sk)-1)
                        sk_id_3 = sk_id_1
                        while (sk_id_3 == sk_id_1 or sk_id_3 == sk_id_2):
                            sk_id_3 = randint(0, len(sk)-1)
                        skills_and_knowledge_html = sk[sk_id_1] + ", " + sk[sk_id_2] + ", " + sk[sk_id_3] + " and " + str(remaining_sk_count) + " other skill"
                        if remaining_sk_count > 1:
                            skills_and_knowledge_html += "s"
                    else:
                        i = 1
                        for skill_or_knowledge in sk:
                            skills_and_knowledge_html += skill_or_knowledge
                            if i + 1 < len(sk):
                                skills_and_knowledge_html += ", "
                            elif i + 1 == len(sk):
                                skills_and_knowledge_html += " and "
                            i += 1
                except Exception:
                    pass

                # Describe and two strengths at work
                try:
                    personality_completed = app_datastore.get_personality(self.session['student_id']).completed
                    trait1 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[0]
                    trait2 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[1]
                    phrase1 = four_temperaments.get_random_at_work(trait1)
                    phrase2 = four_temperaments.get_random_at_work(trait2)
                    strengths_at_work_html = phrase1 + " and " + phrase2
                except Exception:
                    pass

                # Describe existing involvements
                try:
                    involvements = app_datastore.get_experience(self.session['student_id']).involvements
                    experience_completed = app_datastore.get_experience(self.session['student_id']).completed
                    if len(involvements) > 3:
                        remaining_involvement_count = len(involvements) - 3
                        involvement_id_1 = randint(0, len(involvements)-1)
                        involvement_id_2 = involvement_id_1
                        while (involvement_id_2 == involvement_id_1):
                            involvement_id_2 = randint(0, len(involvements)-1)
                        involvement_id_3 = involvement_id_1
                        while (involvement_id_3 == involvement_id_1 or involvement_id_3 == involvement_id_2):
                            involvement_id_3 = randint(0, len(involvements)-1)
                        involvements_html = involvements[involvement_id_1] + ", " + involvements[involvement_id_2] + ", " + involvements[involvement_id_3] + " and " + str(remaining_involvement_count) + " other involvement"
                        if remaining_involvement_count > 1:
                            involvements_html += "s"
                    else:
                        i = 1
                        for involvement in involvements:
                            involvements_html += involvement
                            if i + 1 < len(involvements):
                                involvements_html += ", "
                            elif i + 1 == len(involvements):
                                involvements_html += " or "
                            i += 1
                except Exception:
                    pass

                # Describe any two emotions
                try:
                    personality_completed = app_datastore.get_personality(self.session['student_id']).completed
                    trait1 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[0]
                    trait2 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[1]
                    phrase1 = four_temperaments.get_random_emotion(trait1)
                    phrase2 = four_temperaments.get_random_emotion(trait2)
                    emotions_html = phrase1 + " and " + phrase2
                except Exception:
                    pass

                # Describe any two strengths as a friend
                try:
                    personality_completed = app_datastore.get_personality(self.session['student_id']).completed
                    trait1 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[0]
                    trait2 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[1]
                    phrase1 = four_temperaments.get_random_as_a_friend(trait1)
                    phrase2 = four_temperaments.get_random_as_a_friend(trait2)
                    strengths_as_a_friend_html = phrase1 + " and " + phrase2
                except Exception:
                    pass

                # Describe any best from each dominant trait in terms of personality. There are only two dominant traits out of four.
                try:
                    personality_completed = app_datastore.get_personality(self.session['student_id']).completed
                    trait1 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[0]
                    trait2 = app_datastore.get_personality(self.session['student_id']).two_dominant_temperaments_both[1]
                    phrase1 = four_temperaments.get_random_best_in(trait1)
                    phrase2 = four_temperaments.get_random_best_in(trait2)
                    personality_best_html = phrase1 + " and " + phrase2
                except Exception:
                    pass

                # Describe any one existing advice
                try:
                    advice_html = app_datastore.get_random_advice(self.session['student_id'])
                    experience_completed = app_datastore.get_experience(self.session['student_id']).completed
                except Exception:
                    pass

                # List social networks in bullet points
                try:
                    social_networks_obj = app_datastore.get_user(self.session['student_id']).social_networks
                    for link in social_networks_obj:
                        social_networks_html+="<a href=http://" + link + "><li>http://" + link + "</li></a>"
                except Exception:
                    pass

            # else if the user is new
            else:

                # Register into the datastore
                app_datastore.insert_user(student_profile_object)
                logging.debug(self.session.get('log_identity') + " registered.")
                
            template_values = {
                # Jumbotron
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'matriculation_year': self.session.get('student_matriculation_year'),
                'first_major': self.session.get('student_first_major'),
                'second_major': self.session.get('student_second_major'),
                'faculty': self.session.get('student_faculty'),
                # Summary
                'aspirations_completed': aspirations_completed,
                'education_completed': education_completed,
                'experience_completed': experience_completed,
                'personality_completed': personality_completed,
                'best_modules': best_modules_html,
                'aspirations': aspirations_html,
                'interests': interests_html,
                'skills': skills_and_knowledge_html,
                'two_emotions_from_two_traits': emotions_html,
                'two_strengths_from_two_traits_at_work': strengths_at_work_html,
                'involvements': involvements_html,
                'two_stengths_from_two_traits_as_a_friend': strengths_as_a_friend_html,
                'two_best_from_two_traits': personality_best_html,
                'advice': advice_html,
                # Sidebar
                'gender': app_datastore.get_user(self.session['student_id']).gender,
                'country': app_datastore.get_user(self.session['student_id']).country,
                'date_of_birth': app_datastore.get_user(self.session['student_id']).date_of_birth,
                'website': app_datastore.get_user(self.session['student_id']).website,
                'social_networks': social_networks_html
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
            except Exception:
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
            except Exception:
                pass

            # Retrieve all modules completed by the user from IVLE
            urlfetch.set_default_fetch_deadline(60)
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
            # Retrieve existing user's skills
            skills_html = ''
            try:
                mylist = app_datastore.get_experience(self.session['student_id']).skills_and_knowledge
                for item in mylist:
                    skills_html += "<li>" + item + "</li>"
            except Exception:
                pass

            # Retrieve existing user's interests
            interests_html = ''
            try:
                mylist = app_datastore.get_experience(self.session['student_id']).interests
                for item in mylist:
                    interests_html += "<li>" + item + "</li>"
            except Exception:
                pass

            # Retrieve existing user's involvements
            involvements_html = ''
            try:
                mylist = app_datastore.get_experience(self.session['student_id']).involvements
                for item in mylist:
                    involvements_html += "<li>" + item + "</li>"
            except Exception:
                pass

            # Retrieve existing user's advices
            advices_html = ''
            try:
                mylist = app_datastore.get_experience(self.session['student_id']).advices
                for item in mylist:
                    advices_html += "<li>" + item + "</li>"
            except Exception:
                pass

            # Prepare template values and template
            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'existing_skills': skills_html,
                'existing_interests': interests_html,
                'existing_involvements': involvements_html,
                'existing_advices': advices_html
            }
            template = jinja_environment.get_template('experience.html')

            # Write page
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class Personality(BaseHandler):
    def post(self):
        # Insert or update experience
        skills = self.request.get("skills").split(",,")
        interests = self.request.get("interests").split(",,")
        involvements = self.request.get("involvements").split(",,")
        advices = self.request.get("advices").split(",,")
        if app_datastore.user_exists(self.session['student_id']):
            app_datastore.insert_or_update_experience(self.session['student_id'], skills, interests, involvements, advices)

        # Redirect to Personality questionnaire
        self.redirect(app_domain + "personality")

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
            template_values = analysis.get_symmetrical(self.session['student_id'])
            template_values['student_name'] = self.session.get('student_name')
            template_values['student_email'] = self.session.get('student_email')
            template = jinja_environment.get_template('symmetrical.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ComplementaryConnections(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            template_values = analysis.get_complementary(self.session['student_id'])
            template_values['student_name'] = self.session.get('student_name')
            template_values['student_email'] = self.session.get('student_email')
            template = jinja_environment.get_template('complementary.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)

class ImprovementAdvisory(BaseHandler):
    def get(self):
        if self.session.get('is_valid') == True:
            user_personality = app_datastore.get_personality(self.session['student_id'])

            sanguine_strength_count = user_personality.sanguine_strength_count
            sanguine_weakness_count = user_personality.sanguine_weakness_count
            choleric_strength_count = user_personality.choleric_strength_count
            choleric_weakness_count = user_personality.choleric_weakness_count
            melancholic_strength_count = user_personality.melancholy_strength_count
            melancholic_weakness_count = user_personality.melancholy_weakness_count
            phlegmatic_strength_count = user_personality.phlegmatic_strength_count
            phlegmatic_weakness_count = user_personality.phlegmatic_weakness_count
            sanguine_count = sanguine_strength_count + sanguine_weakness_count
            choleric_count = choleric_strength_count + choleric_weakness_count
            melancholic_count = melancholic_strength_count + melancholic_weakness_count
            phlegmatic_count = phlegmatic_strength_count + phlegmatic_weakness_count

            top_strength = user_personality.two_dominant_temperaments_strength[0]
            second_strength = user_personality.two_dominant_temperaments_strength[1]
            top_weakness = user_personality.two_dominant_temperaments_weakness[0]
            second_weakness = user_personality.two_dominant_temperaments_weakness[1]
            top_both = user_personality.two_dominant_temperaments_both[0]
            second_both = user_personality.two_dominant_temperaments_both[1]

            top_extreme = four_temperaments.get_random_extreme(top_strength)
            second_extreme = four_temperaments.get_random_extreme(second_strength)
            top_flaw = four_temperaments.get_random_flaw(top_weakness)
            second_flaw = four_temperaments.get_random_flaw(second_weakness)
            top_get_along = four_temperaments.get_random_how_to_get_along_with(top_weakness)
            second_get_along = four_temperaments.get_random_how_to_get_along_with(second_weakness)
            top_need = four_temperaments.get_random_needs_to_be(top_both)
            second_need = four_temperaments.get_random_needs_to_be(second_both)
            top_improvement = four_temperaments.get_random_improvement(top_both)
            second_improvement = four_temperaments.get_random_improvement(second_both)

            template_values = {
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'sanguine_strength_count': sanguine_strength_count,
                'sanguine_weakness_count': sanguine_weakness_count,
                'choleric_strength_count': choleric_strength_count,
                'choleric_weakness_count': choleric_weakness_count,
                'melancholic_strength_count': melancholic_strength_count,
                'melancholic_weakness_count': melancholic_weakness_count,
                'phlegmatic_strength_count': phlegmatic_strength_count,
                'phlegmatic_weakness_count': phlegmatic_weakness_count,
                'sanguine_count': sanguine_count,
                'choleric_count': choleric_count,
                'melancholic_count': melancholic_count,
                'phlegmatic_count': phlegmatic_count,
                'top_extreme': top_extreme, 
                'second_extreme': second_extreme, 
                'top_flaw': top_flaw, 
                'second_flaw': second_flaw,
                'top_get_along': top_get_along,
                'second_get_along': second_get_along,
                'top_need': top_need,
                'second_need': second_need,
                'top_improvement': top_improvement,
                'second_improvement': second_improvement
            }
            template = jinja_environment.get_template('improvement.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(app_domain)


class Profile(BaseHandler,blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        student_country = self.request.get('user_country')
        student_gender = self.request.get('user_gender')
        student_website = self.request.get('user_website')
        student_email = self.request.get('user_email')
        student_social_network = self.request.get('networks').split(",,")
        upload_files=self.get_uploads('file')
        if upload_files:
            #do cleanup on the unused blob object
            blob_key=app_datastore.get_pic(self.session.get('student_id'))
            blob_info=blobstore.BlobInfo.get(blob_key)
            blob_info.delete()
            #insert the blob key into the datastore
            blob_info=upload_files[0]
            app_datastore.insert_or_update_pic(self.session.get('student_id'),blob_info.key())
        if self.session.get('is_valid'):
            app_datastore.update_user(self.session.get('student_id'), self.request.get("user_dob"), student_gender, student_country, student_website, student_social_network, student_email)

        self.redirect("/profile")

    def get(self):
        student_obj = app_datastore.get_user(self.session.get('student_id'))
        student_dob = student_obj.date_of_birth
        student_gender = student_obj.gender
        student_country = student_obj.country
        student_website = student_obj.website
        student_email = student_obj.email
        student_social_network = student_obj.social_networks
        networks_html = ''
        upload_url=blobstore.create_upload_url('/profile')
        image=app_datastore.get_pic_url(self.session.get('student_id'))
        try:
            for link in student_social_network:
                networks_html += "<li>" + link + "</li>"
        except Exception:
            pass

        if self.session.get('is_valid') == True:
            template_values = {
                'user_gender': student_gender,
                'student_name': self.session.get('student_name'),
                'student_email': self.session.get('student_email'),
                'user_dob': student_dob,
                'user_country': student_country,
                'user_website': student_website,
                'user_email': student_email,
                'upload_url': upload_url,
                'pic':image,
                'existing_networks': networks_html
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