#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
   integers = int(s)
   a.append(integers)
   s = raw_input()

i = 0
n = 0
while i < len(a):
   if a[i] < n:
   	  n = 1
   i = i + 1

print n
   