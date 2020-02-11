#!/usr/bin/env python3

import sys

number = int(sys.argv[1])

all_numbers = [i for i in range(1, number + 1)]

print("Multiples of 3: {}".format([i for i in all_numbers if i % 3 == 0]))
print("Multiples of 3 squared: {}".format([i ** 2 for i in all_numbers if i % 3 == 0]))
print("Multiples of 4 doubled: {}".format([i * 2 for i in all_numbers if i % 4 == 0]))
print("Multiples of 3 or 4: {}".format([i for i in all_numbers if i % 3 == 0 or i % 4 == 0]))
print("Multiples of 3 and 4: {}".format([i for i in all_numbers if i % 3 == 0 and i % 4 == 0]))
print("Multiples of 3 replaced: {}".format(["X" if i % 3 == 0 else i for i in all_numbers]))
print("Primes: {}".format([p for p in range(2, number) if 0 not in [p % d for d in range(2, p)]]))
