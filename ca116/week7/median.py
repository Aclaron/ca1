#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
   integers = int(s)
   a.append(integers)
   s = raw_input()

i = 0
while i < len(a):
   n = i

   j = i + 1
   while j < len(a):
      if a[j] < a[n]:
         n = j
      j = j + 1

   tmp = a[i]
   a[i] = a[n]
   a[n] = tmp
   i = i + 1

median = 0
i = 0
while i < len(a) / 2 and a[i] != a[len(a) - i - 1]:
   i = i + 1
   median = i

print a[median]
