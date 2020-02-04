#!/usr/bin/env python

s = raw_input()
login = 0
shell = 0

while s != "end":
   i = 0

   while i < len(s) and s[i] != ":":
      i = i + 1

   if i < len(s):
      login = s[:i]

   j = len(s) - 1
   while j < len(s) and s[j] != ":":
      j = j - 1

   if j < len(s):
      shell = s[j + 1:]

   print login, shell
   s = raw_input()
