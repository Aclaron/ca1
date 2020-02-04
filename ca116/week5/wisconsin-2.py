#!/usr/bin/env python

s = raw_input()
total = 0

while s != "end":
   i = 0

   while i < len(s) and s[i] != ",":
      i = i + 1

   if s[i] == "," and s[i + 1] == "W" and s[i + 2] == "I":
      total = total + 1

   s = raw_input()

print total
