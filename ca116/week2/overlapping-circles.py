#!/usr/bin/env python

x1 = input()
y1 = input()
r1 = input()

x2 = input()
y2 = input()
r2 = input()

if (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) < ((r1 + r2) ** 2):
   print "yes"
else:
   print "no"
