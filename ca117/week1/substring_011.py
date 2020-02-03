#!/usr/bin/env python3

import sys

def substring(s):
   seperate = s.split()
   return seperate[0] in seperate[1]

def main():
   for line in sys.stdin:
      checker = substring(line.lower().strip())
      print(checker)

if __name__ == "__main__":
   main()
