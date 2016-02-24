"""
Some IDAT chunks have different filter algorithm ids:
         Type    Name    Meaning
         0       None    11
         1       Sub     010
         2       Up      011
         3       Average 10
         4       Paeth   00
"""
f = open("resudue_filter.txt", "r")
s = ""
for lines in f:
	string = lines[:7]
	for c in string:
		if c == "0":
			s += "11"
		elif c == "1":
			s += "010"
		elif c == "2":
			s += "011"
		elif c == "3":
			s += "10"
		elif c == "4":
			s += "00"
print s,"\n"
answer = ""
while s != "":
	t = s[:8]
	answer += chr(int(t, 2))
	s = s[8:]
print answer
