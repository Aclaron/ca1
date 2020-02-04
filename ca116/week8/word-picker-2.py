#!/usr/bin/env python

string = raw_input()
list1 = []
while string != "end":
   list1.append(string)
   string = raw_input()

position = raw_input()
ostring = ""
olist = []
while position != "end":
   if position != "":
      position = int(position)
      ostring = ostring + " " + list1[position]

   elif position == "":
      olist.append(ostring)
      ostring = ""

   position = raw_input()

if ostring != "":
   olist.append(ostring)

i = 0
while i < len(olist):
   print olist[i][1:]
   i = i + 1
