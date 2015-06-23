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

import urllib2
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

URL = "http://www.xuanran001.com:8080/content/users.1.json"

#
# test
#

class common_Tests(unittest.TestCase):

    def test_common(self):
        xlog( 'Check admin role user list' )
        
        try:
            response = urlopen(URL, timeout = 30)
        except urllib2.HTTPError as e:
            msg = "URL : %s\n" % url
            msg += 'Server return code : %s' % e.code
            self.fail(msg)
        except urllib2.URLError as e:
            self.fail(('Unexpected exception thrown:', e.args))
        except socket.timeout as e:
            self.fail(('Server timeout:', e.args))

        raw_data = response.read().decode('utf-8')
        json_obj = json.loads(raw_data)

        expect = ["congzhiqi@spolo.org",
        "chenyang@masols.com",
        "hanlu@spolo.org",
        "masol.li@gmail.com",
        "wangjingyi@spolo.org"]

        result = []
        for key in json_obj:
            item = json_obj[key]
            if type(item) is dict and "role" in item and item["role"] == "/content/userrole/admin":
                result.append(item["userID"])

        self.assertEqual(expect, result)

def main():

    # create logger
    logger = logging.getLogger('userrole')
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

