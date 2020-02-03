#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
   integers = int(s)
   a.append(integers)
   s = raw_input()

i = 0
smallest = 0
while i < len(a):
   if a[i] < a[smallest]:
      smallest = i
   i = i + 1

print smallest
