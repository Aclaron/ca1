#!/usr/bin/env python3

import sys
import calendar

def birthday(day, month, year):
poem = ["Monday's child is fair of face.",
        "Tuesday's child is full of grace.",
        "Wednesday's child is full of woe.",
        "Thursday's child has far to go.",
        "Friday's child is loving and giving.",
        "Saturday's child works hard for a living.",
        "Sunday's child is fair and wise and good in every way."]

def main():
   for line in sys.stdin:
      print(birthday(s))

if __name__ == "__main__":
   main()