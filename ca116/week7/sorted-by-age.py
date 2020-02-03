#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
   s = s[6:8] + s[3:5] + s[0:2] + s[8:]
   a.append(s)
   s = raw_input()

i = 0
while i < len(a):
   first = i

   j = i + 1
   while j < len(a):
      if a[j] < a[first]:
         first = j
      j = j + 1

   tmp = a[first]
   a[first] = a[i]
   a[i] = tmp

   i = i + 1

i = 0
while i < len(a):
   print a[i][7:]
   i = i + 1
