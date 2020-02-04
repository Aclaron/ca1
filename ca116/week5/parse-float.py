#!/usr/bin/env python

s = raw_input()
t = ""

i = 0
while i < len(s) and s[i] != ".":
   i = i + 1

if s[i] == ".":
   t = t + s[:i]
   print t
   print s[i + 1:]
