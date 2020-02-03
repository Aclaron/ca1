#!/usr/bin/env python

def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp
   return a

def reverse(a):
   i = 0
   while i < len(a) / 2:
      j = len(a) - i - 1
      swap(a, i, j)
      i = i + 1
   return a

if __name__ == "__main__":
   print swap(1, 2, 3)
   print reverse(1)
