#!/usr/bin/env python

n = 5
total = 0
start = 0
s = raw_input()

i = 0
while i < n:
   end = start
   while end < len(s) and s[end] != "+":
      end = end + 1

   total = total + int(s[start:end])
   start = end + 1
   i = i + 1

print total
