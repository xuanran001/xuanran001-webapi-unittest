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
from xxutils import mustHaveProp2
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
URL = "%s/decorationplan/detail3.html?key=%s&id=" %(DOMAIN, KEY)

#
# test
#

class common_Tests(unittest.TestCase):

  def setUp(self):
    xlog("setUp...")

  def test_random_project(self):
    test_single_peojrct(self, "22fcb075-863a-4094-b5e8-0d364e773e3d")
    test_single_peojrct(self, "df058f1f-2a5c-4f4c-b29c-334f79a29e43")

def test_single_peojrct(self, sid):
  url = URL + sid
  print (url)

  response = getjson(self, url)

  # RESPONSE.Result = {}

  self.assertIn("Result", response)
  self.assertIn("projectinfo", response["Result"])
  self.assertIn("shigong", response["Result"])
  self.assertIn("yingzhuang", response["Result"])
  self.assertIn("ruanzhuang", response["Result"])
  self.assertIn("Permission", response)
  self.assertIn("Success", response)
  self.assertTrue("Success", response)

  self.projectinfo = response["Result"]["projectinfo"]
  self.shigong = response["Result"]["shigong"]
  self.yingzhuang = response["Result"]["yingzhuang"]
  self.ruanzhuang = response["Result"]["ruanzhuang"]

  # Trace
  self.trace = {
    "Result" : {}
  }

  test_projectinfo(self)
  test_youhui(self)
  test_shigong(self)
  test_yingzhuang(self)
  test_shejifang(self)
  test_ruanzhuang(self)

def test_projectinfo(self):
  xlog("projectinfo")
  
  projectinfo = self.projectinfo

  # RESPONSE.Result.projectinfo.roominfo = {}

  self.assertIn("roominfo", projectinfo)
  projectinfo_roominfo = projectinfo["roominfo"]

  self.assertIn("ceiling", projectinfo_roominfo)
  self.assertIn("floor", projectinfo_roominfo)

  # RESPONSE.Result.projectinfo.roominfo.details = {}

  self.assertIn("details", projectinfo_roominfo)
  details = projectinfo_roominfo["details"]

  self.assertIn("wall", projectinfo_roominfo)

  self.assertIn("style", projectinfo)
  self.assertIn("name", projectinfo)


  #for result_item in response['Result']:
  #    self.assertIn('id', result_item)
  #
  #    # RESPONSE.Result[0].details = {}
  #    
  #    self.assertIn('details', result_item)
  #    mustHaveProp(self, 'stylename', result_item, URL)

def test_youhui(self):
  xlog("youhui")

def test_shigong(self):
  xlog("shigong")
  self.trace["Result"]["shigong"] = {}
  shigong = self.shigong
  self.assertIn("totalprice", shigong)
  self.assertIn("details", shigong)
  details = shigong["details"]
  self.trace["Result"]["shigong"]["details"] = {}
  for name in details:
    room = details[name]
    self.trace["Result"]["shigong"]["details"][name] = {}
    if name == "自定义":
      pass
    elif name == "水电及其安装与杂项其他":
      pass
    else:
      # Not empty
      self.assertFalse(room == "")
      mustHaveProp2(self, "totalprice", room)
      mustHaveProp2(self, "detail", room)
      room_detail = room["detail"]
      self.trace["Result"]["shigong"]["details"][name]["detail"] = []
      for gongcheng in room_detail:
        self.trace["Result"]["shigong"]["details"][name]["detail"].append(gongcheng["name"]);
        mustHaveProp2(self, "totalprice", gongcheng)
        mustHaveProp2(self, "name", gongcheng)
        mustHaveProp2(self, "unit", gongcheng)
        if gongcheng["name"] == "贴墙面砖":
          print json.dumps(self.trace, indent=2, ensure_ascii=False)
          self.assertTrue(gongcheng["unit"] == "㎡")
        self.trace["Result"]["shigong"]["details"][name]["detail"].pop();
      self.trace["Result"]["shigong"]["details"][name].pop("detail")
    self.trace["Result"]["shigong"]["details"].pop(name)
  self.trace["Result"]["shigong"].pop("details")
  self.trace["Result"].pop("shigong")

def test_yingzhuang(self):
  xlog("yingzhuang")
  self.trace["Result"]["yingzhuang"] = {}
  yingzhuang = self.yingzhuang
  self.assertIn("totalprice", yingzhuang)
  self.assertIn("details", yingzhuang)
  details = yingzhuang["details"]
  self.trace["Result"]["yingzhuang"]["details"] = {}
  for name in details:
    room = details[name]
    self.trace["Result"]["yingzhuang"]["details"][name] = {}
    self.assertFalse(room == "")
    mustHaveProp2(self, "totalprice", room)
    mustHaveProp2(self, "detail", room)
    room_detail = room["detail"]
    self.trace["Result"]["yingzhuang"]["details"][name]["detail"] = []
    for shangpin in room_detail:
      self.trace["Result"]["yingzhuang"]["details"][name]["detail"].append(shangpin["material"]);
      mustHaveProp2(self, "totalprice", shangpin)
      mustHaveProp2(self, "material", shangpin)
      self.trace["Result"]["yingzhuang"]["details"][name]["detail"].pop();
    self.trace["Result"]["yingzhuang"]["details"][name].pop("detail")

def test_shejifang(self):
  xlog("shejifang")

def test_ruanzhuang(self):
  xlog("ruanzhuang")
  self.trace["Result"]["ruanzhuang"] = {}
  ruanzhuang = self.ruanzhuang
  self.assertIn("totalprice", ruanzhuang)
  self.assertIn("details", ruanzhuang)
  details = ruanzhuang["details"]
  self.trace["Result"]["ruanzhuang"]["details"] = {}
  for name in details:
    room = details[name]
    self.trace["Result"]["ruanzhuang"]["details"][name] = {}
    self.assertFalse(room == "")
    mustHaveProp2(self, "totalprice", room)
    mustHaveProp2(self, "detail", room)
    room_detail = room["detail"]
    self.trace["Result"]["ruanzhuang"]["details"][name]["detail"] = []
    for shangpin in room_detail:
      self.trace["Result"]["ruanzhuang"]["details"][name]["detail"].append(shangpin["commodity"]);
      mustHaveProp2(self, "totalprice", shangpin)
      mustHaveProp2(self, "commodity", shangpin)

def main():

  # create logger
  logger = logging.getLogger("decorationplan.detail3")
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

