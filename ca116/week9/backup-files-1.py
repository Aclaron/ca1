#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   curr = files[i]
   if curr[len(curr) - 4:] != ".bak":
      with open(curr) as fd:
         with open(curr + ".bak", "w") as fw:
            fw.write(fd.read())
   i = i + 1
