#!/usr/bin/env python3

import sys

def token_count(s):
   total = 0
   for token in s:
      total = total + 1
   return total

def main():
   total = 0
   for line in sys.stdin:
      s = line.strip().split()
      total = total + token_count(s)
   print(total)

if __name__ == "__main__":
   main()
