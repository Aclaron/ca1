#!/usr/bin/env python3

import sys

def middle(s):
    if len(s) % 2 != 0:
        return(s[len(s) // 2])
    else:
        return('No middle character!')

def main():
   for line in sys.stdin:
      words = middle(line.strip())
      print(words)

if __name__ == "__main__":
   main()
