import urllib2
import json

ivle_api_key = 'O3nIU9c7l8jqYXfBMJlJN'
# The token can be retrieved at https://ivle.nus.edu.sg/api/login/?apikey=O3nIU9c7l8jqYXfBMJlJN
# but it needs authentication. How do I extract the token and pass it to this variable?
ivle_token = ''

ivle_domain = 'https://ivle.nus.edu.sg/'
ivle_api_url = ivle_domain + 'api/lapi.svc/'

def get_student_name():
	# validation_url = ivle_api_url + 'Validate?APIKey=' + ivle_api_key + '&Token=' + ivle_token
	
	student_name_obj = urllib2.urlopen(ivle_api_url + 'UserName_Get?APIKey=' + ivle_api_key + '&Token=' + ivle_token)
	student_name_str = json.load(student_name_obj)
	print "Hello " + student_name_str + "."
	print "Your token is " + ivle_token

get_student_name()
