from google.appengine.ext import ndb
import app_datastore
import difflib

def checkTemperaments(list1,list2):
    for item1 in list1:
        if item1 in list2:
            pass
        else:
            return True

    return False

def get_complementary(std_id):
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
        #check if the 2 temperament are the same
        try:
            other_user_two_temp=app_datastore.get_personality(other_user.student_id).two_dominant_temperaments_both
            if other_user.student_id == std_id:
                pass
            elif(not checkTemperaments(curr_user_two_temp,other_user_two_temp)):
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
                    symmetrical_list[other_user.student_id] = result
                except Exception:
                    pass
        except Exception:
            pass
    sorted_dict=sorted(symmetrical_list,key=symmetrical_list.get, reverse=True)
    result_dict={}
    for x in xrange(0,len(sorted_dict)):
        p_percent='person_'+str(index)+'_percent'
        p_name='person_'+str(index)+'_name'
        p_dob='person_'+str(index)+'_dob'
        p_country='person_'+str(index)+'_country'
        p_major='person_'+str(index)+'_major'
        p_faculty='person_'+str(index)+'_faculty'
        p_skills='person_'+str(index)+'_skills'
        p_interests='person_'+str(index)+'_interests'
        p_involvements='person_'+str(index)+'_involvements'
        p_module='person_'+str(index)+'_best_modules'
        p_advice='person_'+str(index)+'_advice'
        p_aspirations='person_'+str(index)+'_aspirations'
        p_networks='person_'+str(index)+'_networks'
        p_website='person_'+str(index)+'_website'
        result_dict[p_percent]=symmetrical_list.get(sorted_dict[index])
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
        index+=1

    return result_dict
