#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b <= c or a + c <= b or b + c <= a:
   print "no"
else:
   print "yes"
