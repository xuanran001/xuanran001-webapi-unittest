#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#/**************************************************************************
# *
# *  This file is part of the OSC(Open Source Community).
# *  Copyright (C) by SanPolo Co.Ltd. 
# *  All rights reserved.
# *
# *  See http://osc.spolo.org/ for more information.
# *
# *  SanPolo Co.Ltd
# *  http://www.spolo.org/  spolo@spolo.org sales@spolo.org
# *
#**************************************************************************/

import unittest

import json
from urllib2 import urlopen

#reload(sys)
#sys.setdefaultencoding('utf8') 

KEY = "test"
DOMAIN = "http://www.xuanran001.com/api"
URL = "%s/getdesignlist.html?key=%s" %(DOMAIN, KEY)

#
# test
#

class common_Tests(unittest.TestCase):

    def test1(self):
        
        response = urlopen(URL)

        raw_data = response.read().decode('utf-8')
        response = json.loads(raw_data)
        
        self.assertIn('Success', response)
        self.assertEqual(response['Success'], True)
        
        self.assertIn('Count', response)
        
        # RESPONSE.Result = []
        
        self.assertIn('Result', response)
        for result_item in response['Result']:
            self.assertIn('id', result_item)
            self.assertIn('thumbnail', result_item)
            self.assertIn('image', result_item)
            self.assertIn('author', result_item)
            self.assertIn('cameraName', result_item)
            self.assertIn('resolution', result_item)
        
            # RESPONSE.Result[0].details = {}
            
            mustHaveProp(self, 'details', result_item)
            mustHaveProp(self, 'stylename', result_item)
            mustHaveProp(self, 'renderTime', result_item)
            mustHaveProp(self, "hasHDR", result_item)
            mustHaveProp(self, 'canList', result_item)
            mustHaveProp(self, 'jobId', result_item)
            mustHaveProp(self, 'hdr_size', result_item)
            mustHaveProp(self, 'roomname', result_item)
            mustHaveProp(self, 'png_size', result_item)
            mustHaveProp(self, 'createTime', result_item)
            mustHaveProp(self, 'deList', result_item)
            mustHaveProp(self, 'canOpen', result_item)
            mustHaveProp(self, 'hasWatermark', result_item)
            mustHaveProp(self, 'colorname', result_item)
            mustHaveProp(self, 'Time', result_item)
            mustHaveProp(self, 'png_filename', result_item)
            mustHaveProp(self, 'reRender', result_item)
            mustHaveProp(self, 'hdr_filename', result_item)
            mustHaveProp(self, 'keyInfo', result_item)
            
            # RESPONSE.Result[0].details.modelInfos = []
            
            self.assertIn('modelInfos', response['Result'][0]['details'])
            for modelinfo_item in result_item['details']['modelInfos'] :
                self.assertIn('modelname', modelinfo_item)
                self.assertIn('modelId', modelinfo_item)
            
            # RESPONSE.Result[0].details.brandInfos = []
            
            self.assertIn('brandInfos', response['Result'][0]['details'])
            for brandinfo_item in result_item['details']['brandInfos'] :
                self.assertIn('brandname', brandinfo_item)
                self.assertIn('brandpath', brandinfo_item)

    def test_ticket___(self):
        print "Expect : result must have '21' in keyinfo."
        url = URL + "&keyinfo=21"
        print url
        res = getjson(url)
        if res['Count'] is not 0 :
            self.assertIn('21', res['Result'][0]['details']['keyInfo'])

    def test_ticket10128(self):
        msg = "Expect : result must have big and small pic.\n"
        url = URL + "&size=all"
        msg += "URL : %s" % url
        res = getjson(url)
        isAllBig = True
        for item in res['Result'] :
            msg += "Pic resolution is : %s" % item['resolution']
            isAllBig = isAllBig and (item['resolution'] == "1200x900")
        self.assertFalse(isAllBig, msg='{0}'.format(msg))


# get json object from url
def getjson(url):
    response = urlopen(url)
    raw_data = response.read().decode('utf-8')
    return json.loads(raw_data)

# object must have property.
def mustHaveProp(_self, name, item):
    msg = "Expect : must have [%s] property\n" % name
    msg += "ID : %s" % item['id']
    _self.assertIn(name, item['details'], msg='{0}'.format(msg))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

# end

