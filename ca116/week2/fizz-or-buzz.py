#!/usr/bin/env python

n = input()

if n % 5 == 0 and n % 3 == 0:
   print "fizz-buzz"
elif n % 3 == 0:
   print "fizz"
elif n % 5 == 0:
   print "buzz"
elif n % 5 != 0 and n % 3 != 0:
   print n
