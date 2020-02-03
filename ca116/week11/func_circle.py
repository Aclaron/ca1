#!/usr/bin/env python

pi = 3.141

def circumference(r):
   circumference = 2 * pi * r
   return circumference

def area(r):
   area = pi * (r ** 2)
   return area

if __name__ == "__main__":
   print circumference()
   print area()
