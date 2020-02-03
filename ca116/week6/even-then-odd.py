#!/usr/bin/env python

s = raw_input()
a = []
even = []
odd = []

while s != "end":
   integers = int(s)
   a.append(integers)
   if integers % 2 == 0:
      even.append(integers)
   else:
      odd.append(integers)
   s = raw_input()

i = 0
while i < len(even):
   print even[i]
   i = i + 1

i = 0
while i < len(odd):
   print odd[i]
   i = i + 1
