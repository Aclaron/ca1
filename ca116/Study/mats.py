#!/usr/bin/env python

n = input()

if n % 3 == 0:
   print n / 3

else:
   if (n - 1) % 3 == 0:
      new = n - 1
      print new / 3 + 1

   if (n - 2) % 3 == 0:
      new = n - 2
      print new / 3 + 2
