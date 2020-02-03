#!/usr/bin/env python

import sys

lines = sys.stdin.read()
numbers = lines.split()

total = 0
i = 0
while i < len(numbers):
   integers = int(numbers[i])
   total = total + integers
   i = i + 1

print total
