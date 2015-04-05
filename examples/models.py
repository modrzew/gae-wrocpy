import logging

from google.appengine.ext import ndb


class Hello(ndb.Model):
    count = ndb.IntegerProperty(indexed=False, default=0)
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
    children = ndb.KeyProperty(repeated=True)

    def _pre_put_hook(self):
        logging.info('Before putting!')
        self.count += 1

    def _post_put_hook(self):
        logging.info('After putting!')
        self.count += 2


class Container(ndb.Model):
    hello = ndb.StructuredProperty(Hello)
    hello_children = ndb.LocalStructuredProperty(
        Hello,
        repeated=True,
        compressed=True,
    )
    additional_data = ndb.JsonProperty(indexed=True)
    user = ndb.PickleProperty(compressed=True)
