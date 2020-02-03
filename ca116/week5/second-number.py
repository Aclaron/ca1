#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and "0" <= s[j] and s[j] <= "9":
      j = j + 1

if j < len(s):   
   k = j
   while k < len(s) and "0" <= s[k] and s[k] <= "9":
      k = k + 1

if k < len(s):   
   l = k
   while l < len(s) and "0" <= s[l] and s[l] <= "9":
      l = l + 1

   print s[j:k], i + 2
