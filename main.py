import webapp2
import urllib2
class HourlyCronPage(webapp2.RequestHandler):
    def get(self):
        response = urllib2.urlopen('<url_of_your_cloud_function>')
self.response.write(response.read())
app = webapp2.WSGIApplication([
    ('/hourly', HourlyCronPage),
], debug=True)