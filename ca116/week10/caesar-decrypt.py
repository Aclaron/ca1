#!/usr/bin/env python

import sys

line = sys.stdin.read()

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

caesarlower = "nopqrstuvwxyzabcdefghijklm"
caesarupper = "NOPQRSTUVWXYZABCDEFGHIJKLM"

a = []
dictionary = {}

i = 0
while i < 26:
   dictionary[caesarlower[i]] = alphabetlower[i]
   dictionary[caesarupper[i]] = alphabetupper[i]
   i += 1

i = 0
while i < len(line):
   if line[i].isupper() or line[i].islower():
      a.append(dictionary[line[i]])
   else:
      a.append(line[i])
   i += 1

n = "".join(a)
print n,
