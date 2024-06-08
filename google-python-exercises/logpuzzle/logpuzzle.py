#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
from urllib.request import urlopen

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f = open(filename, 'rt', encoding='utf-8')
  d = []
  listjpg = []
  trashlist = []
  extralist = []
  newlist = []
  for line in f:
    match = re.search(r'\s(\S*/puzzle/\S*-(\w\w\w\w).jpg)\s', line)
    match2 = re.search(r'\s(\S*/puzzle/\S*-(\w\w\w\w-(\w\w\w\w)).jpg)\s', line)
    if match2:
      fname = match2.group(1)
      key = match2.group(2)
      code = match2.group(3)
      tuple = (code, fname)
      if key not in extralist:
        trashlist.append(tuple)
        extralist.append(key)
      newlist = sorted(trashlist)
    elif match:
      fname = match.group(1)
      code = match.group(2)
      if code not in trashlist:
        listjpg.append(fname)
        trashlist.append(code)
      sortjpg = sorted(listjpg)
  if len(newlist) > 0:
    for k in newlist:
        o = k[-1]
        listjpg.append(o)
    sortjpg = listjpg
  for a in sortjpg:
    a = 'http://code.google.com/'+a
    d.append(a)
  return d


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  imglist = []
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  l = 0
  for img in img_urls:
    fname = 'img' + str(l)
    filename = os.path.join(dest_dir, fname)
    print('Retrieving: '+img)
    urllib.request.urlretrieve(img, filename)
    imglist.append('<img src="img'+str(l)+'">')
    l= l + 1
  joinlist = ''.join(imglist)
  htmltext = '<html>\n<body>\n'+joinlist+'\n</body>\n</html>'
  htmlpath = os.path.join(dest_dir, 'index.html')
  f = open(htmlpath, 'wt', encoding='utf-8')
  f.write(htmltext)


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)
    
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
