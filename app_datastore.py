# LIBRARIES
from google.appengine.ext import ndb
import datetime




# PROFILE INFORMATION
class ProfileInfo(ndb.Model):
	student_id = ndb.StringProperty()
	date_registered = ndb.DateTimeProperty()
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	matriculation_year = ndb.StringProperty()
	first_major = ndb.StringProperty()
	second_major = ndb.StringProperty()
	faculty = ndb.StringProperty()
	# picture = ndb.BlobKeyProperty()
	date_of_birth = ndb.StringProperty()
	gender = ndb.StringProperty()
	country = ndb.StringProperty()
	website = ndb.StringProperty()
	social_networks = ndb.StringProperty(repeated=True)
	associations = ndb.StringProperty(repeated=True)

def get_user(student_id):
	qry = ProfileInfo.query(ancestor=ndb.Key("NUSBridge", "ProfileInfo"))
	result = qry.filter(ProfileInfo.student_id==student_id).fetch()
	return result[0]

def insert_user(student_profile_object):
	user_key = ndb.Key("NUSBridge", "ProfileInfo")
	nus_user = ProfileInfo(parent=user_key)
	nus_user.student_id = student_profile_object['UserID']
	nus_user.date_registered = datetime.datetime.utcnow()
	nus_user.name = student_profile_object['Name']
	nus_user.email = student_profile_object['Email']
	nus_user.matriculation_year = student_profile_object['MatriculationYear']
	nus_user.first_major = student_profile_object['FirstMajor']
	nus_user.second_major = student_profile_object['SecondMajor']
	nus_user.faculty = student_profile_object['Faculty']
	# nus_user.picture = 
	nus_user.date_of_birth = ''
	nus_user.gender = ''
	nus_user.country = ''
	nus_user.website = ''
	nus_user.social_networks = []
	nus_user.associations = []
	nus_user.put()

def update_user(student_id, user_picture, date_of_birth, gender, country, website, social_networks, associations):
	pass

def user_exists(student_id):
	#user_key = ndb.Key("NUSBridge", entity)
	#temp = ProfileInfo.query(ancestor=user_key)
	#temp.filter(ProfileInfo.student_id==student_id).fetch(0)
	qry = ProfileInfo.query(ancestor=ndb.Key("NUSBridge", "ProfileInfo"))
	result = qry.filter(ProfileInfo.student_id==student_id).fetch()
	if result:
		return True
	else:
		return False

def get_number_of_users():
	return ProfileInfo.query().count()





# ASPIRATIONS
class Aspirations(ndb.Model):
    student_id = ndb.StringProperty()
    aspirations = ndb.StringProperty(repeated=True)

def get_aspirations(student_id):
	qry = Aspirations.query(ancestor=ndb.Key("NUSBridge", "Aspirations"))
	result = qry.filter(Aspirations.student_id==student_id).fetch()
	return result[0]

def insert_or_update_aspirations(student_id, aspirations): # modify this function such that it will insert a new entity if it's new or update the existing entity if present
	user_key = ndb.Key("NUSBridge", "Aspirations")
	user_aspirations = Aspirations(parent=user_key)
	user_aspirations.student_id = student_id
	user_aspirations.aspirations = aspirations
	user_aspirations.put()





# EDUCATION
class Education(ndb.Model):
    student_id = ndb.StringProperty()
    best_modules = ndb.StringProperty(repeated=True)

def get_education(student_id):
	qry = Education.query(ancestor=ndb.Key("NUSBridge", "Education"))
	result = qry.filter(Education.student_id==student_id).fetch()
	return result[0]

def insert_or_update_education(student_id, best_modules): # modify this function such that it will insert a new entity if it's new or update the existing entity if present
	user_key = ndb.Key("NUSBridge", "Education")
	user_education = Education(parent=user_key)
	user_education.student_id = student_id
	user_education.best_modules = best_modules
	user_education.put()





# EXPERIENCE
class Experience(ndb.Model):
    student_id = ndb.StringProperty()
    skills_and_knowledge = ndb.StringProperty(repeated=True)
    interests = ndb.StringProperty(repeated=True)
    involvements = ndb.StringProperty(repeated=True)
    advices = ndb.StringProperty(repeated=True)

def get_experience(student_id):
	qry = Experience.query(ancestor=ndb.Key("NUSBridge", "Experience"))
	result = qry.filter(Experience.student_id==student_id).fetch()
	return result[0]

def insert_or_update_experience(student_id, skills_and_knowledge, interests, involvements, advices): # modify this function such that it will insert a new entity if it's new or update the existing entity if present
	user_key = ndb.Key("NUSBridge", "Experience")
	user_experience = Experience(parent=user_key)
	user_experience.student_id = student_id
	user_experience.skills_and_knowledge = skills_and_knowledge
	user_experience.interests = interests
	user_experience.involvements = involvements
	user_experience.advices = advices
	user_experience.put()






# PERSONALITY
class Personality(ndb.Model):
    student_id = ndb.StringProperty()
    words = ndb.StringProperty(repeated=True)
    word_ids = ndb.IntegerProperty(repeated=True)
    dominant_temperaments = ndb.StringProperty(repeated=True)

def get_personality(std_id):
	qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
	result = qry.filter(Personality.student_id==student_id).fetch()
	return result[0]

def insert_or_update_personality(student_id, words, word_ids, dominant_temperaments): # modify this function such that it will insert a new entity if it's new or update the existing entity if present
	user_key = ndb.Key("NUSBridge", "Personality")
	user_personality = Personality(parent=user_key)
	user_personality.student_id = student_id
	user_personality.words = words
	user_personality.word_ids = word_ids
	user_personality.dominant_temperaments = dominant_temperaments
	user_personality.put()




