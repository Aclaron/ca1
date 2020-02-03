#!/usr/bin/env python

import sys

words = sys.stdin.read().split()

count = {}

i = 0
while i < len(words):
   word = words[i]
   if word not in count:
      count[word] = 0
   count[word] += 1
   i += 1

for word in count:
   if count[word] == 1:
      print word
