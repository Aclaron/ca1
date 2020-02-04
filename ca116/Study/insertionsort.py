#!/usr/bin/env python

i = 1
while i < len(a):
   v = a[i]
   p = i
   
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v

   i = i + 1

print a



linear: O(n), O(n), O(1)
binary: O(log n, O(log n), O(1)

insertion: O(n**2), O(n**2), O(n)
selection: O(n**2), O(n**2), 0(n**2)