#!/usr/bin/env python

n = input()

def fib(n):
   if n == 1:
      return 0
   if n == 2:
      return 1
   if n == 3:
      return 2
   else:
      return fib(n - 1)+ fib(n - 2)

value = n
i = 0

while i < 10000:
   if n <= fib(value):
      value = value - 1
   i = i + 1

print fib(value)
