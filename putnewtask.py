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
import urllib2
from cStringIO import StringIO

from xxutils import getjson
from xxutils import mustHaveProp

from multipartform import MultiPartForm

#reload(sys)
#sys.setdefaultencoding('utf8')

KEY = "test"
URL = "http://www.xuanran001.com/d/api/putnewtask.html"

#
# test
#

class common_Tests(unittest.TestCase):

  def test_1(self):

    # get ip addr
    import socket
    print socket.gethostbyname('www.xuanran001.com')

    # curl example:
    # curl -F key=test -F name="方案名称" -F descope="客厅" -F style="欧式" -F spereq="暂无"  -F huxingtu=@huxingtu.jpg www.xuanran001.com/d/api/putnewtask.html

    # Create the form with simple fields
    form = MultiPartForm()
    form.add_field('key', KEY)
    #form.add_field('umail', '_ceshi87_40wware.org')
    
    # Add a fake file
    #form.add_file('cankaotu[]', 'cankaotu1.jpg', 
    #              fileHandle=StringIO('spolo'))
    #form.add_file('cankaotu[]', 'cankaotu2.jpg', 
    #              fileHandle=StringIO('spolo'))
    #form.add_file('cankaotu[]', 'cankaotu3.jpg', 
    #              fileHandle=StringIO('spolo'))
    form.add_file('huxingtu', 'huxingtu.jpg', 
                  fileHandle=StringIO('spolo'))

    # Build the request
    request = urllib2.Request(URL)
    #request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print
    print 'OUTGOING DATA:'
    print request.get_data()

    print
    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()

def main():
  unittest.main()

if __name__ == '__main__':
  main()

# end
