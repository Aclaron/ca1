#!/usr/bin/env python3

import sys

def camel(s):
   a = []
   for word in s:
      a.append(word[:-1] + word[-1].capitalize())
   string = " ".join(a)
   return string

def main():
   for line in sys.stdin:
      s = line.split()
      print(camel(s))

if __name__ == "__main__":
   main()
