# LIBRARIES
from google.appengine.ext import ndb
from google.appengine.api import images
import datetime
from random import randint
from random import shuffle
import copy
import four_temperaments
from google.appengine.ext import blobstore
import logging



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
    date_of_birth = ndb.StringProperty()
    gender = ndb.StringProperty()
    country = ndb.StringProperty()
    website = ndb.StringProperty()
    social_networks = ndb.StringProperty(repeated=True)


def get_user(student_id):
    qry = ProfileInfo.query(ancestor=ndb.Key("NUSBridge", "ProfileInfo"))
    result = qry.filter(ProfileInfo.student_id == student_id).fetch()
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
    nus_user.date_of_birth = ''
    nus_user.gender = ''
    nus_user.country = ''
    nus_user.website = ''
    nus_user.social_networks = []
    nus_user.put()


def update_user(student_id, email, date_of_birth, gender, country, website, social_networks):
    qry = ProfileInfo.query(ancestor=ndb.Key("NUSBridge", "ProfileInfo"))
    result = qry.filter(ProfileInfo.student_id == student_id).fetch()
    nus_user = result[0]
    nus_user.email = email
    nus_user.date_of_birth = date_of_birth
    nus_user.gender = gender
    nus_user.country = country
    nus_user.website = website
    nus_user.social_networks = social_networks
    nus_user.email=email
    nus_user.put()


def user_exists(student_id):
    qry = ProfileInfo.query(ancestor=ndb.Key("NUSBridge", "ProfileInfo"))
    result = qry.filter(ProfileInfo.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False


def get_number_of_users():
    return ProfileInfo.query().count()


def get_other_records():
    qry = ProfileInfo.query().fetch()
    return qry


def prepare_list(list_of_items):
    temp = ''
    for item in list_of_items:
        temp += item + ', '
    return temp[:-2]


# Picture
class Picture(ndb.Model):
    student_id = ndb.StringProperty()
    image = ndb.BlobKeyProperty()


def insert_or_update_pic(student_id, image_key):
    user_key = ndb.Key("NUSBridge", "Picture")
    qry = Picture.query(ancestor=user_key)
    result=qry.filter(Picture.student_id == student_id).fetch()
    if result:
        user_pic = result[0]
        user_pic.image=image_key
        user_pic.put()
    else:
        user_key = ndb.Key("NUSBridge", "Picture")
        user_pic = Picture(parent=user_key)
        user_pic.student_id = student_id
        user_pic.image = image_key
        user_pic.put()

def get_pic(student_id):
    qry = Picture.query(ancestor=ndb.Key("NUSBridge", "Picture"))
    result = qry.filter(Picture.student_id==student_id).fetch()
    return result[0].image

def pic_exists(student_id):
    qry = Picture.query(ancestor=ndb.Key("NUSBridge", "Picture"))
    result = qry.filter(Picture.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False

def get_pic_url(student_id):
    try:
        image_key=get_pic(student_id)
        image=images.get_serving_url(str(image_key),size=None,crop=False,secure_url=None)
    except Exception:
        student_gender = get_user(student_id).gender
        if student_gender.lower() == 'male':
            image = '../images/male_icon.png'
        elif student_gender.lower() == 'female':
            image = '../images/female_icon.png'
        else:
            image = '../images/student_icon.png'

    return image

# ASPIRATIONS
class Aspirations(ndb.Model):
    student_id = ndb.StringProperty()
    aspirations = ndb.StringProperty(repeated=True)
    completed = ndb.BooleanProperty()


def get_aspirations(student_id):
    qry = Aspirations.query(ancestor=ndb.Key("NUSBridge", "Aspirations"))
    result = qry.filter(Aspirations.student_id == student_id).fetch()
    return result[0]


def insert_or_update_aspirations(student_id, aspirations):
    qry = Aspirations.query(ancestor=ndb.Key("NUSBridge", "Aspirations"))
    result = qry.filter(Aspirations.student_id == student_id).fetch()
    if result:
        user_aspirations = result[0]
        user_aspirations.aspirations = aspirations
        user_aspirations.completed = True
        user_aspirations.put()
    else:
        user_key = ndb.Key("NUSBridge", "Aspirations")
        user_aspirations = Aspirations(parent=user_key)
        user_aspirations.student_id = student_id
        user_aspirations.aspirations = aspirations
        user_aspirations.completed = True
        user_aspirations.put()

def get_all_asp():
    qry = Aspirations.query().fetch()
    temp=[]
    for item in qry:
        for asp in item.aspirations:
            if asp.lower() in temp:
                pass
            else:
                temp.append(asp.lower())
    return prepare_list(temp)

def asp_exists(student_id):
    qry = Aspirations.query(ancestor=ndb.Key("NUSBridge", "Aspirations"))
    result = qry.filter(Aspirations.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False

# EDUCATION
class Education(ndb.Model):
    student_id = ndb.StringProperty()
    best_modules = ndb.StringProperty(repeated=True)
    completed = ndb.BooleanProperty()


def get_education(student_id):
    qry = Education.query(ancestor=ndb.Key("NUSBridge", "Education"))
    result = qry.filter(Education.student_id == student_id).fetch()
    return result[0]


def insert_or_update_education(student_id, best_modules):
    qry = Education.query(ancestor=ndb.Key("NUSBridge", "Education"))
    result = qry.filter(Education.student_id == student_id).fetch()
    if result:
        user_education = result[0]
        user_education.best_modules = best_modules
        user_education.completed = True
        user_education.put()
    else:
        user_key = ndb.Key("NUSBridge", "Education")
        user_education = Education(parent=user_key)
        user_education.student_id = student_id
        user_education.best_modules = best_modules
        user_education.completed = True
        user_education.put()

def education_exists(student_id):
    qry = Education.query(ancestor=ndb.Key("NUSBridge", "Education"))
    result = qry.filter(Education.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False

# EXPERIENCE
class Experience(ndb.Model):
    student_id = ndb.StringProperty()
    skills_and_knowledge = ndb.StringProperty(repeated=True)
    interests = ndb.StringProperty(repeated=True)
    involvements = ndb.StringProperty(repeated=True)
    advices = ndb.StringProperty(repeated=True)
    completed = ndb.BooleanProperty()


def get_experience(student_id):
    qry = Experience.query(ancestor=ndb.Key("NUSBridge", "Experience"))
    result = qry.filter(Experience.student_id == student_id).fetch()
    return result[0]


def insert_or_update_experience(student_id, skills_and_knowledge, interests, involvements, advices):
    qry = Experience.query(ancestor=ndb.Key("NUSBridge", "Experience"))
    result = qry.filter(Experience.student_id == student_id).fetch()
    if result:
        user_experience = result[0]
        user_experience.skills_and_knowledge = skills_and_knowledge
        user_experience.interests = interests
        user_experience.involvements = involvements
        user_experience.advices = advices
        user_experience.completed = True
        user_experience.put()
    else:
        user_key = ndb.Key("NUSBridge", "Experience")
        user_experience = Experience(parent=user_key)
        user_experience.student_id = student_id
        user_experience.skills_and_knowledge = skills_and_knowledge
        user_experience.interests = interests
        user_experience.involvements = involvements
        user_experience.advices = advices
        user_experience.completed = True
        user_experience.put()


def get_number_of_skills(student_id):
    return len(get_experience(student_id).skills_and_knowledge)


def get_number_of_interests(student_id):
    return len(get_experience(student_id).interests)


def get_number_of_advices(student_id):
    return len(get_experience(student_id).advices)


def get_random_advice(student_id):
    return get_experience(student_id).advices[randint(0, get_number_of_advices(student_id) - 1)]

def experience_exists(student_id):
    qry = Experience.query(ancestor=ndb.Key("NUSBridge", "Experience"))
    result = qry.filter(Experience.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False

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
    completed = ndb.BooleanProperty()


def get_personality(student_id):
    qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
    result = qry.filter(Personality.student_id == student_id).fetch()
    return result[0]


def insert_or_update_personality(student_id, words):
    qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
    result = qry.filter(Personality.student_id == student_id).fetch()
    if result:
        user_personality = result[0]
        user_personality.words = words

        # Retrieve index numbers based on selected words and count the number of temperaments
        word_ids = []
        sanguine_strength_count = 0
        sanguine_weakness_count = 0
        choleric_strength_count = 0
        choleric_weakness_count = 0
        melancholic_strength_count = 0
        melancholic_weakness_count = 0
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
            elif temperament == "Melancholic" and sw == "strength":
                melancholic_strength_count += 1
            elif temperament == "Melancholic" and sw == "weakness":
                melancholic_weakness_count += 1
            elif temperament == "Phlegmatic" and sw == "strength":
                phlegmatic_strength_count += 1
            elif temperament == "Phlegmatic" and sw == "weakness":
                phlegmatic_weakness_count += 1

        # Save index numbers based on selected words and count of temperaments
        user_personality.word_ids = word_ids
        user_personality.sanguine_strength_count = sanguine_strength_count
        user_personality.sanguine_weakness_count = sanguine_weakness_count
        user_personality.choleric_strength_count = choleric_strength_count
        user_personality.choleric_weakness_count = choleric_weakness_count
        user_personality.melancholy_strength_count = melancholic_strength_count
        user_personality.melancholy_weakness_count = melancholic_weakness_count
        user_personality.phlegmatic_strength_count = phlegmatic_strength_count
        user_personality.phlegmatic_weakness_count = phlegmatic_weakness_count
        user_personality.put()

        # Get and save top two traits in terms of strengths, weaknesses and both of them
        qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
        result = qry.filter(Personality.student_id == student_id).fetch()
        user_personality = result[0]
        user_personality.two_dominant_temperaments_strength = get_top_two_traits(student_id, "strength")
        user_personality.two_dominant_temperaments_weakness = get_top_two_traits(student_id, "weakness")
        user_personality.two_dominant_temperaments_both = get_top_two_traits(student_id, "both")

        user_personality.completed = True
        user_personality.put()
    else:
        user_key = ndb.Key("NUSBridge", "Personality")
        user_personality = Personality(parent=user_key)
        user_personality.student_id = student_id
        user_personality.words = words

        # Retrieve index numbers based on selected words and count the number of temperaments
        word_ids = []
        sanguine_strength_count = 0
        sanguine_weakness_count = 0
        choleric_strength_count = 0
        choleric_weakness_count = 0
        melancholic_strength_count = 0
        melancholic_weakness_count = 0
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
            elif temperament == "Melancholic" and sw == "strength":
                melancholic_strength_count += 1
            elif temperament == "Melancholic" and sw == "weakness":
                melancholic_weakness_count += 1
            elif temperament == "Phlegmatic" and sw == "strength":
                phlegmatic_strength_count += 1
            elif temperament == "Phlegmatic" and sw == "weakness":
                phlegmatic_weakness_count += 1

        # Save index numbers based on selected words and count of temperaments
        user_personality.word_ids = word_ids
        user_personality.sanguine_strength_count = sanguine_strength_count
        user_personality.sanguine_weakness_count = sanguine_weakness_count
        user_personality.choleric_strength_count = choleric_strength_count
        user_personality.choleric_weakness_count = choleric_weakness_count
        user_personality.melancholy_strength_count = melancholic_strength_count
        user_personality.melancholy_weakness_count = melancholic_weakness_count
        user_personality.phlegmatic_strength_count = phlegmatic_strength_count
        user_personality.phlegmatic_weakness_count = phlegmatic_weakness_count
        user_personality.put()

        # Get and save top two traits in terms of strengths, weaknesses and both of them
        qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
        result = qry.filter(Personality.student_id == student_id).fetch()
        user_personality = result[0]
        user_personality.two_dominant_temperaments_strength = get_top_two_traits(student_id, "strength")
        user_personality.two_dominant_temperaments_weakness = get_top_two_traits(student_id, "weakness")
        user_personality.two_dominant_temperaments_both = get_top_two_traits(student_id, "both")

        user_personality.completed = True
        user_personality.put()


def get_top_two_traits(student_id, swb):
    traits = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]
    trait_count = [0, 0, 0, 0]
    trait_count = [get_temperament_count(student_id, traits[0], swb), get_temperament_count(student_id, traits[1], swb),
                   get_temperament_count(student_id, traits[2], swb), get_temperament_count(student_id, traits[3], swb)]
    sorted_counts = copy.copy(trait_count)
    sorted_counts.sort()
    first_highest_count = sorted_counts[3]
    second_highest_count = sorted_counts[2]
    index_of_first_highest_count_in_trait_count = trait_count.index(first_highest_count)
    index_of_second_highest_count_in_trait_count = trait_count.index(second_highest_count)

    if index_of_second_highest_count_in_trait_count == index_of_first_highest_count_in_trait_count:
        index_of_second_highest_count_in_trait_count += 1
        while (trait_count[index_of_second_highest_count_in_trait_count] != second_highest_count):
            index_of_second_highest_count_in_trait_count += 1

    first_highest_trait = traits[index_of_first_highest_count_in_trait_count]
    second_highest_trait = traits[index_of_second_highest_count_in_trait_count]
    return [first_highest_trait, second_highest_trait]


def get_temperament_count(student_id, temperament, swb):
    if temperament == "Sanguine" and swb == "strength":
        return get_personality(student_id).sanguine_strength_count
    elif temperament == "Sanguine" and swb == "weakness":
        return get_personality(student_id).sanguine_weakness_count
    elif temperament == "Choleric" and swb == "strength":
        return get_personality(student_id).choleric_strength_count
    elif temperament == "Choleric" and swb == "weakness":
        return get_personality(student_id).choleric_weakness_count
    elif temperament == "Melancholic" and swb == "strength":
        return get_personality(student_id).melancholy_strength_count
    elif temperament == "Melancholic" and swb == "weakness":
        return get_personality(student_id).melancholy_weakness_count
    elif temperament == "Phlegmatic" and swb == "strength":
        return get_personality(student_id).phlegmatic_strength_count
    elif temperament == "Phlegmatic" and swb == "weakness":
        return get_personality(student_id).phlegmatic_weakness_count
    elif temperament == "Sanguine" and swb == "both":
        return get_personality(student_id).sanguine_strength_count + get_personality(student_id).sanguine_weakness_count
    elif temperament == "Choleric" and swb == "both":
        return get_personality(student_id).choleric_strength_count + get_personality(student_id).choleric_weakness_count
    elif temperament == "Melancholic" and swb == "both":
        return get_personality(student_id).melancholy_strength_count + get_personality(
            student_id).melancholy_weakness_count
    elif temperament == "Phlegmatic" and swb == "both":
        return get_personality(student_id).phlegmatic_strength_count + get_personality(
            student_id).phlegmatic_weakness_count

def personality_exists(student_id):
    qry = Personality.query(ancestor=ndb.Key("NUSBridge", "Personality"))
    result = qry.filter(Personality.student_id == student_id).fetch()
    if result:
        return True
    else:
        return False