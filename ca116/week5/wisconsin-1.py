#!/usr/bin/env python

s = raw_input()

while s != "end":
   i = 0

   while i < len(s) and s[i] != ",":
      i = i + 1

   if s[i] == "," and s[i + 1] == "W" and s[i + 2] == "I":
      print s[:i]
   s = raw_input()
