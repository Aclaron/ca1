#!/usr/bin/env python

n = input()
t = ""

i = 0
while i < n:
   f = input()
   if i == n - 1:
      t = t + ("*" * f)
   else:
      t = t + ("*" * f) + "\n"
   i = 1 + i
print t
