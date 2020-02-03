#!/usr/bin/env python

s = raw_input()
i = 0
a = []

while s != "end":
   integers = int(s)
   a.append(integers)
   s = raw_input()

n = input()
while i < len(a):
   print a[i] + n
   i = i + 1
