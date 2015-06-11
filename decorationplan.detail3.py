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
from xxutils import xlog
from xxutils import replyticket
from xxutils import paste

import logging
import sys
import random

reload(sys)
sys.setdefaultencoding('utf8')

KEY = "test"
DOMAIN = "http://www.xuanran001.com/api"
ID = "a3960782-c012-4994-8afc-b2950d408769"
URL = "%s/decorationplan/detail3.html?key=%s&id=%s" %(DOMAIN, KEY, ID)

#
# test
#

class common_Tests(unittest.TestCase):

    def test_common(self):
        xlog( 'test_common' )
        
        response = getjson(self, URL)
        
        # RESPONSE.Result = {}

        self.assertIn("Result", response)
        result = response["Result"]

        # RESPONSE.Result.projectinfo = {}

        self.assertIn("projectinfo", result)
        result_projectinfo = result["projectinfo"]

        # RESPONSE.Result.projectinfo.roominfo = {}

        self.assertIn("roominfo", result_projectinfo)
        result_projectinfo_roominfo = result_projectinfo["roominfo"]

        self.assertIn("ceiling", result_projectinfo_roominfo)
        self.assertIn("floor", result_projectinfo_roominfo)

        # RESPONSE.Result.projectinfo.roominfo.details = {}

        self.assertIn("details", result_projectinfo_roominfo)
        details = result_projectinfo_roominfo["details"]

        self.assertIn("wall", result_projectinfo_roominfo)

        self.assertIn("style", result_projectinfo)
        self.assertIn("name", result_projectinfo)

        # RESPONSE.Permission = {}

        self.assertIn("Permission", response)

        # RESPONSE.Success = bool

        self.assertIn("Success", response)
        self.assertTrue("Success", response)

        #for result_item in response['Result']:
        #    self.assertIn('id', result_item)
        #
        #    # RESPONSE.Result[0].details = {}
        #    
        #    self.assertIn('details', result_item)
        #    mustHaveProp(self, 'stylename', result_item, URL)
            
def main():

    # create logger
    logger = logging.getLogger('getdesignlist')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler( sys.__stdout__ ) # Add this
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')
    
    unittest.main()

if __name__ == '__main__':
    main()

# end

