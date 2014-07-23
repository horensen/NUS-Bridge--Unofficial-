from google.appengine.ext import ndb
import app_datastore
import difflib
import logging

def similar_temperaments(list1,list2):
    for item1 in list1:
        if item1 in list2:
            pass
        else:
            return False

    return True

def get_symmetrical(std_id):
    # populate the list of user to be compare with
    compare_list = app_datastore.get_other_records()
    symmetrical_list = {}
    index=0
    num_of_matching_asp = 0
    total_num_of_compare_std_asp = 0
    num_of_matching_personality = 0
    #loop through the list to find the common connection
    curr_user_asp_list = app_datastore.get_aspirations(std_id).aspirations
    curr_user_personality_list = app_datastore.get_personality(std_id).words
    curr_user_two_temp=app_datastore.get_personality(std_id).two_dominant_temperaments_both
    #for loop each item for each other user
    for other_user in compare_list:
        if (app_datastore.aspiration_exists(other_user.student_id) and app_datastore.personality_exists(other_user.student_id) and app_datastore.experience_exists(other_user.student_id) and app_datastore.education_exists(other_user.student_id)):
            try:
                other_user_two_temp=app_datastore.get_personality(other_user.student_id).two_dominant_temperaments_both
                if other_user.student_id == std_id:
                    pass
                elif(not similar_temperaments(curr_user_two_temp,other_user_two_temp)):
                    pass
                else:
                    num_of_matching_asp = 0
                    total_num_of_compare_std_asp = 0
                    num_of_matching_personality = 0
                    try:
                        other_asp = app_datastore.get_aspirations(other_user.student_id).aspirations
                        other_personality = app_datastore.get_personality(other_user.student_id).words
                        #count the aspiration part
                        for asp in curr_user_asp_list:
                            compare = difflib.get_close_matches(asp, other_asp, n=20, cutoff=0.8)
                            num_of_matching_asp += len(compare)
                        total_num_of_compare_std_asp = len(other_asp)
                        #count the personality part
                        for personality in curr_user_personality_list:
                            compare = difflib.get_close_matches(personality, other_personality, n=40, cutoff=1)
                            num_of_matching_personality += len(compare)
                            #cal using the formula then include the user if more than 80
                        formula = float((float(num_of_matching_asp / total_num_of_compare_std_asp) + float(
                            num_of_matching_personality / 40.0)) / 2.0) * 100.0
                        result = round(formula, 1)
                        symmetrical_list[other_user.student_id] = result
                    except Exception:
                        pass
            except Exception:
                pass
        #check if the 2 temperament are the same
        else:
            pass
            
    sorted_dict=sorted(symmetrical_list,key=symmetrical_list.get, reverse=True)
    result_dict={}
    place_index=0
    for x in xrange(0,len(sorted_dict)):
        place_index=x+1
        p_percent='person_'+str(place_index)+'_percent'
        p_name='person_'+str(place_index)+'_name'
        p_dob='person_'+str(place_index)+'_dob'
        p_gender='person_'+str(place_index)+'_gender'
        p_country='person_'+str(place_index)+'_country'
        p_major='person_'+str(place_index)+'_major'
        p_faculty='person_'+str(place_index)+'_faculty'
        p_skills='person_'+str(place_index)+'_skills'
        p_interests='person_'+str(place_index)+'_interests'
        p_involvements='person_'+str(place_index)+'_involvements'
        p_module='person_'+str(place_index)+'_best_modules'
        p_advice='person_'+str(place_index)+'_advice'
        p_aspirations='person_'+str(place_index)+'_aspirations'
        p_networks='person_'+str(place_index)+'_networks'
        p_website='person_'+str(place_index)+'_website'
        p_pic='person_'+str(place_index)+'_pic'
        p_email='person_'+str(place_index)+'_email'
        result_dict[p_percent]=int(round(symmetrical_list.get(sorted_dict[index])))
        result_dict[p_name]=app_datastore.get_user(sorted_dict[index]).name
        result_dict[p_dob]=app_datastore.get_user(sorted_dict[index]).date_of_birth
        result_dict[p_gender]=app_datastore.get_user(sorted_dict[index]).gender
        result_dict[p_country]=app_datastore.get_user(sorted_dict[index]).country
        result_dict[p_major]=app_datastore.get_user(sorted_dict[index]).first_major
        if (app_datastore.get_user(sorted_dict[index]).second_major != ''):
            result_dict[p_major] += " and " + app_datastore.get_user(sorted_dict[index]).second_major
        result_dict[p_faculty]=app_datastore.get_user(sorted_dict[index]).faculty
        result_dict[p_skills]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).skills_and_knowledge)
        result_dict[p_interests]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).interests)
        result_dict[p_involvements]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).involvements)
        result_dict[p_module]=app_datastore.prepare_list(app_datastore.get_education(sorted_dict[index]).best_modules)
        result_dict[p_advice]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).advices)
        result_dict[p_aspirations]=app_datastore.prepare_list(app_datastore.get_aspirations(sorted_dict[index]).aspirations)
        result_dict[p_networks]=app_datastore.prepare_list(app_datastore.get_user(sorted_dict[index]).social_networks)
        result_dict[p_website]=app_datastore.get_user(sorted_dict[index]).website
        result_dict[p_pic]=app_datastore.get_pic_url(sorted_dict[index])
        result_dict[p_email]=app_datastore.get_user(sorted_dict[index]).email
        index+=1

    return result_dict

def different_temperaments(list1,list2):
    for item1 in list1:
        if item1 in list2:
            pass
        else:
            return True

    return False

def get_complementary(std_id):
    # populate the list of user to be compare with
    compare_list = app_datastore.get_other_records()
    complementary_list = {}
    index=0
    num_of_matching_asp = 0
    total_num_of_compare_std_asp = 0
    num_of_matching_personality = 0
    #loop through the list to find the common connection
    curr_user_asp_list = app_datastore.get_aspirations(std_id).aspirations
    curr_user_personality_list = app_datastore.get_personality(std_id).words
    curr_user_two_temp=app_datastore.get_personality(std_id).two_dominant_temperaments_both
    #for loop each item for each other user
    for other_user in compare_list:
        if (app_datastore.aspiration_exists(other_user.student_id) and app_datastore.personality_exists(other_user.student_id) and app_datastore.experience_exists(other_user.student_id) and app_datastore.education_exists(other_user.student_id)):
            try:
                other_user_two_temp=app_datastore.get_personality(other_user.student_id).two_dominant_temperaments_both
                if other_user.student_id == std_id:
                    pass
                elif(not different_temperaments(curr_user_two_temp,other_user_two_temp)):
                    pass
                else:
                    num_of_matching_asp = 0
                    total_num_of_compare_std_asp = 0
                    num_of_matching_personality=0
                    num_of_not_matching_personality = 0
                    try:
                        other_asp = app_datastore.get_aspirations(other_user.student_id).aspirations
                        other_personality = app_datastore.get_personality(other_user.student_id).words
                        #count the aspiration part
                        for asp in curr_user_asp_list:
                            compare = difflib.get_close_matches(asp, other_asp, n=20, cutoff=0.8)
                            num_of_matching_asp += len(compare)
                        total_num_of_compare_std_asp = len(other_asp)
                        #count the personality part
                        for personality in curr_user_personality_list:
                            compare = difflib.get_close_matches(personality, other_personality, n=40, cutoff=1)
                            num_of_matching_personality += len(compare)
                            #cal using the formula then include the user if more than 80
                        num_of_not_matching_personality=40-num_of_matching_personality
                        formula = float((float(num_of_matching_asp / total_num_of_compare_std_asp) + float(
                            num_of_not_matching_personality / 40.0)) / 2.0) * 100.0
                        result = round(formula, 1)
                        complementary_list[other_user.student_id] = result
                    except Exception:
                        pass
            except Exception:
                pass
        else:
            pass
        
    sorted_dict=sorted(complementary_list,key=complementary_list.get, reverse=True)
    result_dict={}
    place_index=0
    for x in xrange(0,len(sorted_dict)):
        place_index=x+1
        p_percent='person_'+str(place_index)+'_percent'
        p_name='person_'+str(place_index)+'_name'
        p_dob='person_'+str(place_index)+'_dob'
        p_country='person_'+str(place_index)+'_country'
        p_major='person_'+str(place_index)+'_major'
        p_faculty='person_'+str(place_index)+'_faculty'
        p_skills='person_'+str(place_index)+'_skills'
        p_interests='person_'+str(place_index)+'_interests'
        p_involvements='person_'+str(place_index)+'_involvements'
        p_module='person_'+str(place_index)+'_best_modules'
        p_advice='person_'+str(place_index)+'_advice'
        p_aspirations='person_'+str(place_index)+'_aspirations'
        p_networks='person_'+str(place_index)+'_networks'
        p_website='person_'+str(place_index)+'_website'
        p_email='person_'+str(place_index)+'_email'
        p_pic='person_'+str(place_index)+'_pic'
        result_dict[p_percent]=int(round(complementary_list.get(sorted_dict[index])))
        result_dict[p_name]=app_datastore.get_user(sorted_dict[index]).name
        result_dict[p_dob]=app_datastore.get_user(sorted_dict[index]).date_of_birth
        result_dict[p_country]=app_datastore.get_user(sorted_dict[index]).country
        result_dict[p_major]=app_datastore.get_user(sorted_dict[index]).first_major
        if (app_datastore.get_user(sorted_dict[index]).second_major != ''):
            result_dict[p_major] += " and " + app_datastore.get_user(sorted_dict[index]).second_major
        result_dict[p_faculty]=app_datastore.get_user(sorted_dict[index]).faculty
        result_dict[p_skills]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).skills_and_knowledge)
        result_dict[p_interests]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).interests)
        result_dict[p_involvements]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).involvements)
        result_dict[p_module]=app_datastore.prepare_list(app_datastore.get_education(sorted_dict[index]).best_modules)
        result_dict[p_advice]=app_datastore.prepare_list(app_datastore.get_experience(sorted_dict[index]).advices)
        result_dict[p_aspirations]=app_datastore.prepare_list(app_datastore.get_aspirations(sorted_dict[index]).aspirations)
        result_dict[p_networks]=app_datastore.prepare_list(app_datastore.get_user(sorted_dict[index]).social_networks)
        result_dict[p_website]=app_datastore.get_user(sorted_dict[index]).website
        result_dict[p_pic]=app_datastore.get_pic_url(sorted_dict[index])
        result_dict[p_email]=app_datastore.get_user(sorted_dict[index]).email
        index+=1

    return result_dict
