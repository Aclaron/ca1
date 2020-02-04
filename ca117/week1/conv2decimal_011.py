#!/usr/bin/env python3

import sys

def convert(number, base):
   base = int(base)
   number = int(number, base)
   return number

def main():
   for line in sys.stdin:
      [number, base] = line.split()
      print(convert(number, base))

if __name__ == "__main__":
   main()
