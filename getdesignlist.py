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
        
        self.assertIn('Result', response)
        self.assertIn('id', response['Result'][0])
        self.assertIn('thumbnail', response['Result'][0])
        self.assertIn('image', response['Result'][0])
        self.assertIn('author', response['Result'][0])
        self.assertIn('cameraName', response['Result'][0])
        self.assertIn('resolution', response['Result'][0])
        
        self.assertIn('details', response['Result'][0])
        self.assertIn('stylename', response['Result'][0]['details'])
        self.assertIn('renderTime', response['Result'][0]['details'])
        self.assertIn('hasHDR', response['Result'][0]['details'])
        self.assertIn('canList', response['Result'][0]['details'])
        self.assertIn('jobId', response['Result'][0]['details'])
        self.assertIn('hdr_size', response['Result'][0]['details'])
        self.assertIn('roomname', response['Result'][0]['details'])
        self.assertIn('png_size', response['Result'][0]['details'])
        self.assertIn('createTime', response['Result'][0]['details'])
        self.assertIn('deList', response['Result'][0]['details'])
        self.assertIn('canOpen', response['Result'][0]['details'])
        self.assertIn('hasWatermark', response['Result'][0]['details'])
        self.assertIn('colorname', response['Result'][0]['details'])
        self.assertIn('Time', response['Result'][0]['details'])
        self.assertIn('png_filename', response['Result'][0]['details'])
        self.assertIn('reRender', response['Result'][0]['details'])
        self.assertIn('hdr_filename', response['Result'][0]['details'])
        self.assertIn('keyInfo', response['Result'][0]['details'])
        
        self.assertIn('modelInfos', response['Result'][0]['details'])
        self.assertIn('modelname', response['Result'][0]['details']['modelInfos'][0])
        self.assertIn('modelId', response['Result'][0]['details']['modelInfos'][0])
        
        self.assertIn('brandInfos', response['Result'][0]['details'])
        self.assertIn('brandname', response['Result'][0]['details']['brandInfos'][0])
        self.assertIn('brandpath', response['Result'][0]['details']['brandInfos'][0])


def main():
    unittest.main()

if __name__ == '__main__':
    main()

# end

