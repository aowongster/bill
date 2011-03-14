#!/usr/bin/python
# File Name: setup.py
# Created:   23-02-2011

import sys

def main(argv):
  """main func"""
  try:
    from setuptools import setup
  except ImportError:
    from distutils.core import setup

  config = {
    'description': 'Project Name',
    'author': 'My Name',
    'url': 'Homepage url',
    'download_url': 'Download url',
    'author_email': 'my email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bill'],
    'scripts': [],
    'name': 'projectname'
  }
  setup(**config)

if __name__ == "__main__":
  sys.exit(main(sys.argv))

