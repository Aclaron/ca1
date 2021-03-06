#!/usr/bin/env python3

import math
import sys

def pi(n):
   return "{:.{}f}".format(math.pi, n)

def main():
   n = sys.argv[1]
   print(pi(n))

if __name__ == "__main__":
   main()
