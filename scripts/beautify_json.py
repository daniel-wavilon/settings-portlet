#!/usr/bin/env python
"""
Convert all JSON data files in the current tree to human-readable form.

Usage:
  beautify_json.py [-o|--overwrite] [-h|--help]

If overwrite is specified, files will be overwritten in place.

"""

import sys
import simplejson as json
import tempfile
import getopt

import fnmatch
import os

def beautify_json(json_in):
  json_out = json.dumps(json.loads(json_in), indent=4)
  return json_out

def find_files(top_level, pattern):
  matches = []
  for root, dirnames, filenames in os.walk(top_level):
    for filename in fnmatch.filter(filenames, pattern):
      matches.append(os.path.join(root, filename))
  return matches

def beautify_all(overwrite=False):
  files = find_files(".", "*.json")
  for f in files:
    h = open(f)
    beautiful_json = beautify_json(h.read())
    h.close()
    if overwrite :
      h = open(f, "w")
      h.write(beautiful_json)
      h.write("\n")
      print "File %-50s has been beautified" % (f)
    else:
      tmp = tempfile.NamedTemporaryFile(delete=False)
      tmp.write(beautiful_json)
      tmp.write("\n")
      print "%-50s > %s" % (f, tmp.name)

def usage():
    print __doc__
    
def process_options(argv):
  overwrite = False
  h         = False
  try:
    opts, args = getopt.getopt(argv[1:], "oh", ['overwrite', 'help'])
  except getopt.GetoptError, err:
    # print help information and exit:
    print str(err)
    usage()
    sys.exit(2)
  for o, a in opts:
    if o in ("-o", "--overwrite"):
      overwrite = True
    elif o in ("-h", "--help"):
      h = True
  return overwrite, h

overwrite, h = process_options(sys.argv)
if h :
  usage()
  sys.exit(0)

beautify_all(overwrite)
sys.exit(0)
