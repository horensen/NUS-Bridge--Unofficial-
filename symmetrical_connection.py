import app_datastore
import difflib


def get(self):
    # populate the list of user to be compare with
    compare_list = app_datastore.get_other_records()
    symmetrical_list = {}
    symmetrical_percent = []
    result_sort_list = '<table>'
    num_of_matching_asp = 0
    total_num_of_compare_std_asp = 0
    num_of_matching_personality = 0
    #loop through the list to find the common connection
    curr_user_asp_list = app_datastore.get_aspirations(self.session.get('student_id')).aspirations
    curr_user_personality_list = app_datastore.get_personality(self.session.get('student_id')).words
    #for loop each item for each other user
    for other_user in compare_list:
        if other_user.student_id == self.session.get('student_id'):
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
                symmetrical_list[result] = other_user
                symmetrical_percent.append(result)
            except Exception:
                pass
    symmetrical_percent.sort()
    sym_last_index = len(symmetrical_percent) - 1
    if self.session.get('is_valid') == True:
        template_values = {
            'student_name': self.session.get('student_name'),
            'student_email': self.session.get('student_email'),
            'person_1_percent': symmetrical_percent[sym_last_index],
            'person_1_name': symmetrical_list[symmetrical_percent[sym_last_index]].name,
            'person_1_dob': symmetrical_list[symmetrical_percent[sym_last_index]].date_of_birth,
            'person_1_country': symmetrical_list[symmetrical_percent[sym_last_index]].country,
            'person_1_major': symmetrical_list[symmetrical_percent[sym_last_index]].first_major,
            'person_1_faculty': symmetrical_list[symmetrical_percent[sym_last_index]].faculty,
            'person_1_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index]].student_id).skills_and_knowledge),
            'person_1_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index]].student_id).interests),
            'person_1_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index]].student_id).involvements),
            'person_1_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index]].student_id).best_modules),
            'person_1_advice': app_datastore.prepare_list(
                app_datastore.get_experience(symmetrical_list[symmetrical_percent[sym_last_index]].student_id).advices),
            'person_1_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index]].student_id).aspirations),
            'person_1_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index]].social_networks),
            'person_2_percent': symmetrical_percent[sym_last_index - 1],
            'person_2_name': symmetrical_list[symmetrical_percent[sym_last_index - 1]].name,
            'person_2_dob': symmetrical_list[symmetrical_percent[sym_last_index - 1]].date_of_birth,
            'person_2_country': symmetrical_list[symmetrical_percent[sym_last_index - 1]].country,
            'person_2_major': symmetrical_list[symmetrical_percent[sym_last_index - 1]].first_major,
            'person_2_faculty': symmetrical_list[symmetrical_percent[sym_last_index - 1]].faculty,
            'person_2_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).skills_and_knowledge),
            'person_2_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).interests),
            'person_2_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).involvements),
            'person_2_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).best_modules),
            'person_2_advice': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).advices),
            'person_2_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].student_id).aspirations),
            'person_2_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index - 1]].social_networks),
            'person_3_percent': symmetrical_percent[sym_last_index - 2],
            'person_3_name': symmetrical_list[symmetrical_percent[sym_last_index - 2]].name,
            'person_3_dob': symmetrical_list[symmetrical_percent[sym_last_index - 2]].date_of_birth,
            'person_3_country': symmetrical_list[symmetrical_percent[sym_last_index - 2]].country,
            'person_3_major': symmetrical_list[symmetrical_percent[sym_last_index - 2]].first_major,
            'person_3_faculty': symmetrical_list[symmetrical_percent[sym_last_index - 2]].faculty,
            'person_3_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).skills_and_knowledge),
            'person_3_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).interests),
            'person_3_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).involvements),
            'person_3_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).best_modules),
            'person_3_advice': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).advices),
            'person_3_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].student_id).aspirations),
            'person_3_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index - 2]].social_networks),
            'person_4_percent': symmetrical_percent[sym_last_index - 3],
            'person_4_name': symmetrical_list[symmetrical_percent[sym_last_index - 3]].name,
            'person_4_dob': symmetrical_list[symmetrical_percent[sym_last_index - 3]].date_of_birth,
            'person_4_country': symmetrical_list[symmetrical_percent[sym_last_index - 3]].country,
            'person_4_major': symmetrical_list[symmetrical_percent[sym_last_index - 3]].first_major,
            'person_4_faculty': symmetrical_list[symmetrical_percent[sym_last_index - 3]].faculty,
            'person_4_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).skills_and_knowledge),
            'person_4_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).interests),
            'person_4_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).involvements),
            'person_4_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).best_modules),
            'person_4_advice': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).advices),
            'person_4_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].student_id).aspirations),
            'person_4_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index - 3]].social_networks),
            'person_5_percent': symmetrical_percent[sym_last_index - 4],
            'person_5_name': symmetrical_list[symmetrical_percent[sym_last_index - 4]].name,
            'person_5_dob': symmetrical_list[symmetrical_percent[sym_last_index - 4]].date_of_birth,
            'person_5_country': symmetrical_list[symmetrical_percent[sym_last_index - 4]].country,
            'person_5_major': symmetrical_list[symmetrical_percent[sym_last_index - 4]].first_major,
            'person_5_faculty': symmetrical_list[symmetrical_percent[sym_last_index - 4]].faculty,
            'person_5_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).skills_and_knowledge),
            'person_5_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).interests),
            'person_5_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).involvements),
            'person_5_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).best_modules),
            'person_5_advice': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).advices),
            'person_5_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].student_id).aspirations),
            'person_5_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index - 4]].social_networks),
            'person_6_percent': symmetrical_percent[sym_last_index - 5],
            'person_6_name': symmetrical_list[symmetrical_percent[sym_last_index - 5]].name,
            'person_6_dob': symmetrical_list[symmetrical_percent[sym_last_index - 5]].date_of_birth,
            'person_6_country': symmetrical_list[symmetrical_percent[sym_last_index - 5]].country,
            'person_6_major': symmetrical_list[symmetrical_percent[sym_last_index - 5]].first_major,
            'person_6_faculty': symmetrical_list[symmetrical_percent[sym_last_index - 5]].faculty,
            'person_6_skills': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).skills_and_knowledge),
            'person_6_interests': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).interests),
            'person_6_involvements': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).involvements),
            'person_6_best_modules': app_datastore.prepare_list(app_datastore.get_education(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).best_modules),
            'person_6_advice': app_datastore.prepare_list(app_datastore.get_experience(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).advices),
            'person_6_aspirations': app_datastore.prepare_list(app_datastore.get_aspirations(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].student_id).aspirations),
            'person_6_networks': app_datastore.prepare_list(
                symmetrical_list[symmetrical_percent[sym_last_index - 5]].social_networks)
        }

