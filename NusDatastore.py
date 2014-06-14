import urllib
import webapp2
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers


class ProfileInfo(ndb.Model):
	student_id=ndb.StringProperty()
	name=ndb.StringProperty()
	#picture=ndb.BlobKeyProperty()
	email=ndb.StringProperty()
	matric_yr=ndb.StringProperty()
	first_major=ndb.StringProperty()
	second_major=ndb.StringProperty()
	faculty=ndb.StringProperty()
	country=ndb.StringProperty()
	gender=ndb.StringProperty()
	#dob=ndb.DateProperty()
	social_network=ndb.StringProperty(repeated=True)
	assoc_list=ndb.StringProperty(repeated=True)

class Aspirations(ndb.Model):
    student_id=ndb.StringProperty()
    content=ndb.StringProperty(repeated=True)

class Education(ndb.Model):
    student_id=ndb.StringProperty()
    list_of_mod=ndb.StringProperty(repeated=True)

class Experience(ndb.Model):
    student_id=ndb.StringProperty()
    list_of_skills_and_knowledge=ndb.StringProperty(repeated=True)
    list_of_advices_or_wisdoms=ndb.StringProperty(repeated=True)
    list_of_interest=ndb.StringProperty(repeated=True)
    list_of_achievements=ndb.StringProperty(repeated=True)

class PersonalityTest(ndb.Model):
    student_id=ndb.StringProperty()
    question_list=ndb.IntegerProperty(repeated=True)
    type1=ndb.StringProperty()
    type2=ndb.StringProperty()


def userExist(std_id):
	user_key=ndb.Key("NUSBridge", "ProfileInfo")
	temp=ProfileInfo.query(ProfileInfo.student_id==std_id).fetch()
	if not temp:
		return False
	else:
		return True
def createUser(student_obj):
	# Also include timestamp
	user_key=ndb.Key("NUSBridge", "ProfileInfo")
	nus_user= ProfileInfo(parent=user_key)
	nus_user.student_id=student_obj['UserID']
	nus_user.name=student_obj['Name']
	nus_user.email=student_obj['Email']
	nus_user.matric_yr=student_obj['MatriculationYear']
	nus_user.first_major=student_obj['FirstMajor']
	nus_user.second_major=student_obj['SecondMajor']
	nus_user.faculty=student_obj['Faculty']
	nus_user.country=''
	nus_user.gender=''
	#nus_user.dob=''
	nus_user.social_network=[]
	nus_user.assoc_list=[]
	nus_user.put()