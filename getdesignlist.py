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

#
# test
#

class common_Tests(unittest.TestCase):

    def test1(self):
        
        key = "test"
        url = "http://www.xuanran001.com/api/getdesignlist.html?key=%s" % key
        response = urlopen(url)

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
            
            self.assertIn('details', result_item)
            self.assertIn('stylename', result_item['details'])
            self.assertIn('renderTime', result_item['details'])
            self.assertIn('hasHDR', result_item['details'])
            self.assertIn('canList', result_item['details'])
            self.assertIn('jobId', result_item['details'])
            self.assertIn('hdr_size', result_item['details'])
            self.assertIn('roomname', result_item['details'])
            self.assertIn('png_size', result_item['details'])
            self.assertIn('createTime', result_item['details'])
            self.assertIn('deList', result_item['details'])
            self.assertIn('canOpen', result_item['details'])
            self.assertIn('hasWatermark', result_item['details'])
            self.assertIn('colorname', result_item['details'])
            self.assertIn('Time', result_item['details'])
            self.assertIn('png_filename', result_item['details'])
            self.assertIn('reRender', result_item['details'])
            self.assertIn('hdr_filename', result_item['details'])
            self.assertIn('keyInfo', result_item['details'])
            
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


def main():
    unittest.main()

if __name__ == '__main__':
    main()

# end

