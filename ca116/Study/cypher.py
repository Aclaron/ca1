#!/usr/bin/env python

s = "cab"

cypher = {
   "a": "b",
   "b": "c",
   "c": "a",
}

def encode(cypher, s):
   ss = ""

   i = 0
   while i < len(s):
      if s[i] in cypher:
         ss = ss + cypher[s[i]]
      else:
         ss = ss + s[i]
      i = i + 1

   return ss

print encode(cypher, "cab")
