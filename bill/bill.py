#!/usr/bin/python
# File Name: bill.py
# Created:   13-03-2011

import sys
import os
import time
import argparse

""" Commands: bill cmd
new - start a new timer
start timer_name - begin timer
stop - stops running timer
printout - prints billable report
"""

__BILLDIR = os.path.join(os.path.expanduser('~'), '.bill')

def get_today():
  now = time.localtime()
  tfmt = '%a, %d %b %Y'
  return time.strftime(tfmt, now)

def writen(fp, str):
  """ write to file with newline """
  fp.write(str +'\n')

def start():
  """ start timer on report """

def stop():
  """ stop timer on running report """

def new():
  """ create a new timer and report """
  name = raw_input('Enter report name: ')
  # get some fancy dir stuff
  if not os.path.isdir(__BILLDIR):
    print('Making folder ' + __BILLDIR)
    os.mkdir(__BILLDIR)

  try:
    fname = __BILLDIR+ '/' +name+ '.bill'

    dtstring = get_today()

    fp = open(fname, 'w')
    # fp.write('Report: '+name +'\n')
    # fp.write('Date started: ' + dtstring+'\n')
    writen(fp,'Report: '+name)
    writen(fp,'Date started: ' + dtstring)
    fp.close()
  except IOError:
    print('Could not create the report')
    raise
  else:
    print('Report Successfully created.')

def printout():
  """ print formatted info on timer """

def main(argv):
  """main func"""
  parser = argparse.ArgumentParser(description='Create a timer and report.')
  parser.add_argument('cmd', help='the command for bill to execute. Possible choices for cmd are: start, stop, new, printout. Workflow: new, begins a new report. Start starts the timing, stop will stop the timer, printout returns the timer information')
  args = parser.parse_args()
  cmd = args.cmd

  if cmd == 'start':
    pass
  elif cmd == 'stop':
    pass
  elif cmd == 'new':
    new()
  elif cmd == 'printout':
    pass
  else:
    parser.print_help()

  # do stuff

if __name__ == "__main__":
  sys.exit(main(sys.argv))

