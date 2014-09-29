#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.api import urlfetch
from decimal import Decimal
 

import webapp2
import jinja2
import os
import json


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#End of Libraries



class MainHandler(webapp2.RequestHandler):
    def get(self):
            url_linktext = 'Login'
            template_values = {
                'url': "url",
                'url_linktext': url_linktext,
            }
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render(template_values))

class getdata(webapp2.RequestHandler):
    def get(self):
        #set URl to get data from
        url="http://www.quandl.com/api/v1/datasets/BITCOIN/BITSTAMPUSD.json"
        # Fetch transactions from url
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            content_json=json.loads(result.content)
            ignorelist = ["20110930","20111001","20111002","20111015","20111016","20111018","20111019","20111022","20111023","20111027","20111102","20111103","20111107","20111123","20111127","2011120","20111204","20111209","20111217"]
            for dayinfo in reversed(content_json["data"]):
                if dayinfo[0].encode('ascii','ignore').replace("-","") not in ignorelist:
                    self.response.write(dayinfo[0].encode('ascii','ignore').replace("-",""))
                    self.response.write(";")
                    self.response.write(round(dayinfo[1],2))
                    self.response.write(";")
                    self.response.write(round(dayinfo[2],2))
                    self.response.write(";")
                    self.response.write(round(dayinfo[3],2))
                    self.response.write(";")
                    self.response.write(round(dayinfo[4],2))
                    self.response.write(";")
                    #if int(round(dayinfo[5])) != '0':
                    self.response.write(int(round(dayinfo[5])))
                    #else:
                        #self.response.write("1")
                    self.response.write("<BR>")

                
            #self.response.write(data)
            
        
        #json_result=json.loads(result.content)
        #blockchain_transacctions=json_result["txs"]
        #self.response.write(type(blockchain_transacctions).__name__)
        #for blockchain_transacction in blockchain_transacctions:
        






app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getdata', getdata),
], debug=True)
