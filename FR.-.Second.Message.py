"""
used pngcheck to extract IDAT chunk sizes which are char codes
"""

f = open('residue.txt', 'r')
print f
answer = ""
for line in f:
	answer += chr(int(line[39:]))
print answer
