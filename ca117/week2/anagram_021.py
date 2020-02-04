#!/usr/bin/env python3

import sys

def anagram(s):
   if sorted(s[0]) == sorted(s[1]):
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      a = line.split()
      print(anagram(a))

if __name__ == "__main__":
   main()
