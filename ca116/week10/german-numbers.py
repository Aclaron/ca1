#!/usr/bin/env python

import sys

words = sys.stdin.readlines()
german = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

i = 0
while i < len(words):
   word = words[i].rstrip()
   if word in german:
      print german[word]
   i += 1
