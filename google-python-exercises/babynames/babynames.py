#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'rt', encoding='utf-8')
  d = {}
  listnames = []
  for line in f:
    match = re.search(r'(<tr align="right"><td>(\d*)</td><td>(\w+)</td><td>(\w+)</td>)', line)
    match2 = re.search(r'Popularity\sin\s(\d\d\d\d)', line)
    if match2:
      d['year'] = match2.group(1)
      y = d['year']
    if match:
      d[match.group(2)] = (match.group(3), match.group(4))
  
  for key in d:
    names = d[key]
    listnames.append((names[0], key))
    if names[1]:
      listnames.append((names[1], key))
  listnames.pop(0)
  listnames.pop(0)
  sortednames = [y]+ sorted(listnames)
  return sortednames
  #for item in sortednames:
    #return(item.type())
def summary_file(filename):
  print(' ')
  

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary:
    for html in args:
      sortednames = extract_names(html)
      newfile = html + '.summary'
      f = open(newfile, 'wt', encoding='utf-8')
      year = sortednames.pop(0)+'\n'
      f.write(year)
      for item in sortednames:
        l = item[0]+' '+item[1]+'\n'
        f.write(l)
      
  else:
    sortednames = extract_names(args[0])
    print(sortednames.pop(0))
    for item in sortednames:
      print(item[0], item[1])

if __name__ == '__main__':
  main()
