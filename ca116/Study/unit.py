#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
longest_line = ""

i = 0
while i < len(lines):
   if len(longest_line) < len(lines[i]):
      longest_line = lines[i]
   i = i + 1

print longest_line,
