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
from urllib2 import HTTPError

#reload(sys)
#sys.setdefaultencoding('utf8')

# get json object from url
def getjson(_self, url):
    try:
        response = urlopen(url)
    except HTTPError as e:
        _self.fail(('Server return code : ', e.code))
    except e:
        _self.fail(('Unexpected exception thrown:', e))
        
    raw_data = response.read().decode('utf-8')
    return json.loads(raw_data)

# object must have property.
def mustHaveProp(_self, name, item, url):
    msg = "Expect : must have [%s] property\n" % name
    msg += "ID : %s\n" % item['id']
    msg += "URL : %s" % url
    _self.assertIn(name, item['details'], msg='{0}'.format(msg))
