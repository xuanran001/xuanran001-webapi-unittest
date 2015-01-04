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
import socket
import os

import logging

#reload(sys)
#sys.setdefaultencoding('utf8')

# get json object from url
def getjson(_self, url):
    try:
        response = urlopen(url, timeout = 30)
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
    _self.assertEqual(json_obj['Success'], True, msg="{0}".format("Success in json is not true, and response json : "+str(json_obj)))

    return json_obj

def paste(obj):
    try:
        data = "paste_data=%s&paste_lang=javascript&api_submit=true&mode=json"%json.dumps(obj)
        response = urlopen("http://fpaste.org/", data = data, timeout = 30)
    except urllib2.HTTPError as e:
        msg = "URL : %s\n" % url
        msg += 'Server return code : %s' % e.code
        print msg
    except urllib2.URLError as e:
        print 'Unexpected exception thrown:', e.args
    except socket.timeout as e:
        print 'Server timeout:', e.args
        
    raw_data = response.read().decode('utf-8')
    json_obj = json.loads(raw_data)

    print json_obj

    return "http://fpaste.org/%s" % json_obj["result"]["id"]
# object must have property.
def mustHaveProp(_self, name, item, url):
    msg = "Expect : must have [%s] property\n" % name
    msg += "ID : %s\n" % item['id']
    msg += "URL : %s\n" % url
    _self.assertIn(name, item['details'], msg='{0}'.format(msg))

def xlog(str):
    logger = logging.getLogger("getdesignlist")
    logger.debug( str )

def replyticket(ticketid, ticketcomment):
    cmd = "./replyticket.sh \"%s\" '%s'" % (ticketid, ticketcomment)
    
    #just debug
    print '[xxutils.py] replyticket cmd = ', cmd

    os.system(cmd)

#EOF
