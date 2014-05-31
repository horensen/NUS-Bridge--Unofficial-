import cgi
import urllib

import webapp2

from google.appengine.ext import ndb

class UserName(ndb.Model):
	name=ndb.StringProperty()
	
class UserDisplay(webapp2.RequestHandler):
	user1=UserName(name="Peter").put()
	user2=UserName(name="John").put()
	user3=UserName(name="Sandy").put()
	
	def post(self):
		user_name=self.request.get('username')
		if(user_name!=None):
			result=UserName.query(name=user_name).fetch()
			if result:
				self.response.out.write('%s is a registered user'%(result))
			else:
				self.response.out.write('%s is a not a registered user'%(result))
		else:
			self.response.out.write('No input is detected.')
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/profile', StudentProfile),
							   ('/testNdb', )],
                              debug=True)