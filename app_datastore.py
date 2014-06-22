# LIBRARIES
from google.appengine.ext import ndb
import datetime
import four_temperaments




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

def update_user(student_id, user_picture, date_of_birth, gender, country, website, social_networks, associations): # implement this function
	pass

def user_exists(student_id): # this function is modified
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

#my sugguestion of implementing the update by having individual method for each field
def updateUserRecord():
	





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

def get_number_of_skills(student_id): # implement this function
	return 0

def get_number_of_interests(student_id): # implement this function
	return 0






# PERSONALITY
class Personality(ndb.Model):
    student_id = ndb.StringProperty()
    words = ndb.StringProperty(repeated=True)
    word_ids = ndb.IntegerProperty(repeated=True)
    sanguine_strength_count = ndb.IntegerProperty()
    sanguine_weakness_count = ndb.IntegerProperty()
    choleric_strength_count = ndb.IntegerProperty()
    choleric_weakness_count = ndb.IntegerProperty()
    melancholy_strength_count = ndb.IntegerProperty()
    melancholy_weakness_count = ndb.IntegerProperty()
    phlegmatic_strength_count = ndb.IntegerProperty()
    phlegmatic_weakness_count = ndb.IntegerProperty()
    two_dominant_temperaments_strength = ndb.StringProperty(repeated=True)
    two_dominant_temperaments_weakness = ndb.StringProperty(repeated=True)
    two_dominant_temperaments_both = ndb.StringProperty(repeated=True)

def insert_or_update_personality(student_id, words): # modify this function such that it will insert a new entity if it's new or update the existing entity if present
	user_key = ndb.Key("NUSBridge", "Personality")
	user_personality = Personality(parent=user_key)
	user_personality.student_id = student_id
	user_personality.words = words
	word_ids = []
	sanguine_strength_count = 0
	sanguine_weakness_count = 0
	choleric_strength_count = 0
	choleric_weakness_count = 0
	melancholy_strength_count = 0
	melancholy_weakness_count = 0
	phlegmatic_strength_count = 0
	phlegmatic_weakness_count = 0
	for word in words:
		word_id = four_temperaments.get_word_id(word)
		temperament = four_temperaments.get_temperament(word)
		sw = four_temperaments.get_strength_or_weakness(word)
		word_ids.append(word_id)
		if temperament == "Sanguine" and sw == "strength":
			sanguine_strength_count += 1
		elif temperament == "Sanguine" and sw == "weakness":
			sanguine_weakness_count += 1
		elif temperament == "Choleric" and sw == "strength":
			choleric_strength_count += 1
		elif temperament == "Choleric" and sw == "weakness":
			choleric_weakness_count += 1
		elif temperament == "Melancholy" and sw == "strength":
			melancholy_strength_count += 1
		elif temperament == "Melancholy" and sw == "weakness":
			melancholy_weakness_count += 1
		elif temperament == "Phlegmatic" and sw == "strength":
			phlegmatic_strength_count += 1
		elif temperament == "Phlegmatic" and sw == "weakness":
			phlegmatic_weakness_count += 1
	user_personality.word_ids = word_ids
	user_personality.sanguine_strength_count = sanguine_strength_count
	user_personality.sanguine_weakness_count = sanguine_weakness_count
	user_personality.choleric_strength_count = choleric_strength_count
	user_personality.choleric_weakness_count = choleric_weakness_count
	user_personality.melancholy_strength_count = melancholy_strength_count
	user_personality.melancholy_weakness_count = melancholy_weakness_count
	user_personality.phlegmatic_strength_count = phlegmatic_strength_count
	user_personality.phlegmatic_weakness_count = phlegmatic_weakness_count
	# implement here to store the
	# - two dominant temperaments (strength)
	# - two dominant temperaments (weakness)
	# - two dominant temperaments (both strength and weakness)
	user_personality.put()

def get_percentage(temperament, swb): # implement this function
	if temperament == "Sanguine" and swb == "strength":
		return 0 / 20
	elif temperament == "Sanguine" and swb == "weakness":
		return 0 / 20
	elif temperament == "Choleric" and swb == "strength":
		return 0 / 20
	elif temperament == "Choleric" and swb == "weakness":
		return 0 / 20
	elif temperament == "Melancholy" and swb == "strength":
		return 0 / 20
	elif temperament == "Melancholy" and swb == "weakness":
		return 0 / 20
	elif temperament == "Phlegmatic" and swb == "strength":
		return 0 / 20
	elif temperament == "Phlegmatic" and swb == "weakness":
		return 0 / 20
	elif temperament == "Sanguine" and swb == "both":
		return 0 / 40
	elif temperament == "Choleric" and swb == "both":
		return 0 / 40
	elif temperament == "Melancholy" and swb == "both":
		return 0 / 40
	elif temperament == "Phlegmatic" and swb == "both":
		return 0 / 40
