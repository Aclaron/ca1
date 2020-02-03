#!/usr/bin/env python3

import sys

def password(s):
   digit_count = 0
   upper_count = 0
   lower_count = 0
   special_count = 0

   for c in s:
      if c.isdigit():
         digit_count = 1
      elif c.isupper():
         upper_count = 1
      elif c.islower():
         lower_count = 1
      else:
         special_count = 1

   return digit_count + upper_count + lower_count + special_count

def main():
   for line in sys.stdin:
      s = line.strip()
      print(password(s))

if __name__ == "__main__":
   main()
