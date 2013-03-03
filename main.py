import webapp2
import urllib

from google.appengine.ext.webapp import template
from google.appengine.api import memcache

SEARCH_URL = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyD_Z_KKtug50dgk7BFZF_KTvLr2b6IaEY8&country=US&q=%s&alt=json"

class SearchHandler(webapp2.RequestHandler):
	def get(self):
		query = self.request.get("q")
		data = memcache.get(query)
		if not data:
			data = urllib.urlopen(SEARCH_URL % query).read()
			memcache.set(query, data)

		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.write(data)

app = webapp2.WSGIApplication(
	[
		('/search', SearchHandler),
	], debug=True)
