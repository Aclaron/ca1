#!/usr/bin/env python

s = raw_input()

def maximum(s):
   highest = s[0]
   for number in s:
      if highest < number:
         highest = number
   return highest

print maximum([4,10,1,7])
