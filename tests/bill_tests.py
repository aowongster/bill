#!/usr/bin/python

from nose.tools import *
import bill

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_basic():
  print "I RAN!"
