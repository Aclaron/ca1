#!/usr/bin/env python

f = raw_input()
s = raw_input()
t = raw_input()

if len(f) > len(s) and len(f) > len(t):
   print f
if len(s) > len(t) and len(s) > len(f):
   print s
if len(t) > len(s) and len(t) > len(f):
   print t
