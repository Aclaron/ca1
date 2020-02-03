#!/usr/bin/env python3

import sys

def chop(s):
   return s[1:len(s) - 1]

def main():
   for line in sys.stdin:
      s = line.strip()
      if len(s) > 1:
         output = s[0].capitalize() + chop(s) + s[-1].capitalize()
         print(output)

if __name__ == "__main__":
   main()
