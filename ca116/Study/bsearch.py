#!/usr/bin/env python

def bsearch(a,q):
   p = 0
   i = 0
   while i < len(a):
      if a[i] < q:
         p = p + 1
         i = i + 1
      if a[i] >= q:
         return p

print bsearch([1,2,3,4,5,6,7,15,27,345],18)
