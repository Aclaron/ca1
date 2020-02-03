#!/usr/bin/env python

i = 0

while i < n:
   s = raw_input()
   i = i + 1

   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1

   num1 = int(s[:j])
   num2 = int(s[j + 1:])

   if num1 + num2 == 1000:
      exit()

   print num1 + num2
