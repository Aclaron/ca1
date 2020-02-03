#!/usr/bin/env python

total = 0
pluses = 0

while pluses < 5:
   s = raw_input()
   pluses = pluses + 1

   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1
      total = total + int(s[:j]) + int (s[j + 1:])

   print total
