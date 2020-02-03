#!/usr/bin/env python

if __name__ == "__main__":
   a = []

i = 0
while i < len(a):
   if len(a[i]) < 6:
      i = i + 1
   elif len(a[i]) >= 6:
      print a[i]
      i = i + 1
