#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as fd:
      numbers = fd.readline()
      while numbers:
         integers = int(numbers)
         total = total + integers
         numbers = fd.readline()
   i = i + 1

print total
