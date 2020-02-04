#!/usr/bin/env python

def maximum(s):
   highest = s[0]
   i = 0
   while i < len(s):
      if highest < s[i]:
         highest = s[i]
      i = i + 1
   return highest

print maximum([10,987,288,353,12,5373473,3])