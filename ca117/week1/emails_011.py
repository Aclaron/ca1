#!/usr/bin/env python3

import sys

def email(s):
   no_email = ""
   first_name = ""
   second_name_numbers = ""
   second_name = ""
   remove_second_name_numbers = []

   for c in s:
      no_email = " ".join(s)
      no_email = no_email.split("@")[0].split(".")
      first_name = no_email[0].capitalize()
      second_name_numbers = no_email[1].capitalize()

   for number in second_name_numbers:
      if not number.isdigit():
         remove_second_name_numbers.append(number)
   second_name = "".join(remove_second_name_numbers)

   return first_name + " " + second_name

def main():
   for line in sys.stdin:
      s = line.split()
      print(email(s))

if __name__ == "__main__":
   main()
