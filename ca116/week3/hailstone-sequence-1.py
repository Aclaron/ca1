#!/usr/bin/env python

n = input()
m = input()
print m

i = 0
while i < n - 1:
   if m % 2 == 1:
      m = ((m * 3) + 1)
   elif m % 2 == 0:
      m = (m / 2)
   print m
   i = i + 1
