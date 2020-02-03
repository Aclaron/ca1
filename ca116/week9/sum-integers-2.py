#!/usr/bin/env python

import sys

file_name = sys.argv[1]
with open(file_name) as fd:
   numbers = fd.readlines()

total = 0
i = 0
while i < len(numbers):
   integers = int(numbers[i])
   total = total + integers
   i = i + 1

print total
