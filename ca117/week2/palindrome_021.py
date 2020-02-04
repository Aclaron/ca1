#!/usr/bin/env python3

import sys

def palindrome(s):
   new_string = ""
   for c in s:
      if c.isalnum():
         new_string = new_string + c

   reverse_string = new_string[::-1]

   if reverse_string.lower() == new_string.lower():
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      s = line.strip()
      print(palindrome(s))

if __name__ == "__main__":
   main()
