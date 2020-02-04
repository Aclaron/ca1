#!/usr/bin/env python3

import sys

unique_words = []

def unique(s):
   all_words = []
   for word in s:
      if word[-1].isalnum():
         all_words.append(word)
      else:
         all_words.append(word[:-1])

   for unique_word in all_words:
      if unique_word not in unique_words:
         unique_words.append(unique_word)
   return len(unique_words)

def main():
   for line in sys.stdin:
      unique(line.lower().strip().split())
   print(len(unique_words) - 1)

if __name__ == "__main__":
   main()
