#!/usr/bin/env python

s = raw_input()

while s != "end":
   i = 0

   while i < len(s) and s[i] != ",":
      i = i + 1

   if s[i] == "," and s[i - 1] == "y" and s[i - 2] == "t" \
      and s[i - 3] == "i" and s[i - 4] == "C" and s[i - 5] == " ":

      print s[:i]

   s = raw_input()
