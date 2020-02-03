#!/usr/bin/env python3

import sys
import math

def main():
   s = sys.stdin.readlines()
   maxlength = len(s[0].strip())
   for k in s:
      k = k.strip()
      if len(k.strip()) > maxlength:
         maxlength = len(k.strip())
   for i in s:
      print("{:^{}s}".format(i.strip(), maxlength))

if __name__ == "__main__":
   main()
