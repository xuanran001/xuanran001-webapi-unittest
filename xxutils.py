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

import logging

#reload(sys)
#sys.setdefaultencoding('utf8')

# get json object from url
def getjson(_self, url):
    try:
        response = urlopen(url)
    except urllib2.HTTPError as e:
        msg = "URL : %s\n" % url
        msg += 'Server return code : %s' % e.code
        _self.fail(msg)
    except urllib2.URLError as e:
        _self.fail(('Unexpected exception thrown:', e.args))
    except socket.timeout as e:
        _self.fail(('Server timeout:', e.args))
        
    raw_data = response.read().decode('utf-8')
    json_obj = json.loads(raw_data)

    _self.assertIn('Success', json_obj)
    _self.assertEqual(json_obj['Success'], True, msg="{0}".format("response json : "+str(json_obj)))

    return json_obj

# object must have property.
def mustHaveProp(_self, name, item, url):
    msg = "Expect : must have [%s] property\n" % name
    msg += "ID : %s\n" % item['id']
    msg += "URL : %s\n" % url
    _self.assertIn(name, item['details'], msg='{0}'.format(msg))

def xlog(str):
    logger = logging.getLogger("getdesignlist")
    logger.debug( str )
