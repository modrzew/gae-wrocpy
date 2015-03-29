import webapp2


class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hi! I\'m running inside webapp2!')


application = webapp2.WSGIApplication([
    webapp2.Route(
        '/',
        HelloWorldHandler,
    ),
])
