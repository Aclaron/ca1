#!/usr/bin/env python3

import sys

def contains(s1, s2):
   s1 = s1.lower()
   s2 = s2.lower()
   for word in s1:
      if word in s2:
         s2 = s2.replace(word, "")
      else:
         return False
   return True

def main():
   for line in sys.stdin:
      s = line.split()
      output = contains(s[0], s[1])
      print(output)

if __name__ == "__main__":
   main()
