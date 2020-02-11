#!/usr/bin/env python3

import sys

def main():
   try:
      with open(sys.argv[1]) as f:
         bestmark = - 1
         for line in f:
            mark, name = line.strip().split(" ", 1)
            if bestmark < int(mark):
               bestmark, beststudent = int(mark), name
            elif int(mark) == bestmark:
               beststudent = beststudent + ", " + name
      print("Best student(s):", beststudent)
      print("Best mark:", bestmark)

   except FileNotFoundError:
      print("The file", sys.argv[1], "could not be opened.")

if __name__ == '__main__':
   main()
