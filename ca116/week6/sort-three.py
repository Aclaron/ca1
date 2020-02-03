#!/usr/bin/env python

a = []

i = 0
while i < 3:
   a.append(input())
   i = i + 1

i = 0
maximum = i
while i < len(a):
   if a[maximum] < a[i]:
      maximum = i
   i = i + 1

i = 0
minimum = i
while i < len(a):
   if a[i] < a[minimum]:
      minimum = i
   i = i + 1

i = 0
middle = i
while i < len(a):
   if i != minimum and i != maximum:
      middle = i
   i = i + 1

print a[minimum]
print a[middle]
print a[maximum]
