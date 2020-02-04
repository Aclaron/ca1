s = raw_input()

i = 0
while i < len(s) and s[i] == s[len(s) - i]:
   i = i + 1

if i <= len(s):
   print "no"

else:
   print "yes"
