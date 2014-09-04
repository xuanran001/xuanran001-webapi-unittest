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

from xxutils import getjson
from xxutils import mustHaveProp

#reload(sys)
#sys.setdefaultencoding('utf8')

KEY = "test"
DOMAIN = "http://www.xuanran001.com/api"
URL = "%s/getdesignlist.html?key=%s" %(DOMAIN, KEY)

#
# test
#

class common_Tests(unittest.TestCase):

    def test_common(self):
        
        response = getjson(self, URL)
        
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
            
            self.assertIn('details', result_item)
            mustHaveProp(self, 'stylename', result_item, URL)
            mustHaveProp(self, 'renderTime', result_item, URL)
            mustHaveProp(self, 'canList', result_item, URL)
            mustHaveProp(self, 'jobId', result_item, URL)
            mustHaveProp(self, 'roomname', result_item, URL)
            mustHaveProp(self, 'createTime', result_item, URL)
            mustHaveProp(self, 'deList', result_item, URL)
            mustHaveProp(self, 'canOpen', result_item, URL)
            mustHaveProp(self, 'colorname', result_item, URL)
            mustHaveProp(self, 'Time', result_item, URL)
            mustHaveProp(self, 'reRender', result_item, URL)
            mustHaveProp(self, 'keyInfo', result_item, URL)
            
            mustHaveProp(self, 'hasWatermark', result_item, URL)
            if result_item['details']['hasWatermark'] is False :
                mustHaveProp(self, 'png_size', result_item, URL)
                mustHaveProp(self, 'png_filename', result_item, URL)
            
            mustHaveProp(self, "hasHDR", result_item, URL)
            if result_item['details']['hasHDR'] is True :
                mustHaveProp(self, 'hdr_size', result_item, URL)
                mustHaveProp(self, 'hdr_filename', result_item, URL)
            
            # RESPONSE.Result[0].details.modelInfos = []
            
            self.assertIn('modelInfos', result_item['details'])
            for modelinfo_item in result_item['details']['modelInfos'] :
                self.assertIn('modelname', modelinfo_item)
                self.assertIn('modelId', modelinfo_item)
            
            # RESPONSE.Result[0].details.brandInfos = []
            
            self.assertIn('brandInfos', result_item['details'])
            for brandinfo_item in result_item['details']['brandInfos'] :
                self.assertIn('brandname', brandinfo_item)
                self.assertIn('brandpath', brandinfo_item)

class param_Tests(unittest.TestCase):

    # test limit param from 1 to 3.
    def test_param_limit(self):
        lmt = 1
        while lmt < 4:
            url = URL + "&limit=" + str(lmt)
            res = getjson(self, url)
            self.assertTrue(len(res['Result']) == lmt)
            lmt += 1
    
    def test_param_size_small(self):
        msg = "Expect : pic size must be 480x360.\n"
        url = URL + "&size=small"
        msg += "URL : %s\n" % url
        res = getjson(self, url)
        isAllSmall = True
        for item in res['Result'] :
            msg += "Pic resolution is : %s\n" % item['resolution']
            isAllSmall = isAllSmall and (item['resolution'] == "480x360")
        self.assertTrue(isAllSmall, msg='{0}'.format(msg))

    def test_param_size_big(self):
        msg = "Expect : pic size must be 1200x900.\n"
        url = URL + "&size=big"
        msg += "URL : %s\n" % url
        res = getjson(self, url)
        isAllBig = True
        for item in res['Result'] :
            msg += "Pic resolution is : %s\n" % item['resolution']
            isAllBig = isAllBig and (item['resolution'] == "1200x900")
        self.assertTrue(isAllBig, msg='{0}'.format(msg))


class bug_Tests(unittest.TestCase):

    def test_ticket10133(self):
        msg = "Expect : result must have '21' in keyinfo.\n"
        url = URL + "&keyinfo=21"
        msg += "URL : %s" % url
        res = getjson(self, url)
        info = []
        info.append(res['Result'][0]['details']['keyInfo'])
        info.append(res['Result'][0]['cameraName'])
        if res['Count'] is not 0 :
            self.assertIn('21', info, msg='{0}'.format(msg))

    def test_ticket10128(self):
        msg = "Expect : result must have big and small pic.\n"
        url = URL + "&size=all"
        msg += "URL : %s" % url
        res = getjson(self, url)
        isAllBig = True
        for item in res['Result'] :
            msg += "Pic resolution is : %s" % item['resolution']
            isAllBig = isAllBig and (item['resolution'] == "1200x900")
        self.assertFalse(isAllBig, msg='{0}'.format(msg))



def main():
    unittest.main()

if __name__ == '__main__':
    main()

# end

