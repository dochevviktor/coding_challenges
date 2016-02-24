import time
import sys

"""
Goal here is to decrypt cipher by brute force
Using bytes seemed to improve speed to a certain degree

"""

cipher =[0x5499fa99, 0x1ee7d8da, 0x5df0b78b, 0x1cb0c18c, 0x10f09fc5, 0x4bb7fdae, 0x7fcb95ac,
           0xe494fbae, 0x8f5d90a3, 0xc766fdd7, 0xb7399ecc, 0xbf4af592, 0xf35c9dc2, 0x272be2a4,
           0x5e788697, 0x520febd8, 0x468c808c, 0x2e550ac9, 0x2b4d28b7, 0x4c166789, 0x33df0bec,
           0x67a96778, 0x0ffa0ce3, 0x44cd2a9a, 0x2dc208dc, 0x35c26a9d, 0x658b0fd7, 0x0d006482,
           0x46c90cf8, 0x28d72a79, 0x4ea94be5, 0x1bbc6995, 0x478505d3, 0x7b1a6b8d, 0xaf7408db,
           0xef7d7f9f, 0x76471cc6, 0xef1076b4, 0x6c911aa7, 0xe75a7ed3, 0x89630c8d, 0xf32b7fcb,
           0x697c1e89, 0x091c30be, 0x736a4cbf, 0xe27339bb, 0x9a2a52a2]

text = [""]*46
try:
    i1 = int(sys.argv[1])
except:
    print ("A number from 0 to 3 needs to be specified as an argument (use DFCL2-Pypy Launcher.bat)!")
    sys.exit()
answer = ""
test = "2074686520" # = (space)the(space)
flag = 0x0

# Deny Range (for now its easier to check, mmk ?)
deny = {"0"}

for i in xrange(0,31):
    deny.add(hex(i).lstrip("0x"))
for i in xrange(121,256):
    deny.add(hex(i).lstrip("0x"))
deny = frozenset(deny)
program_starts = time.time()
# 0x2710 = 10000
# 0x7530 = 30000
# 0xc350 = 50000
iter_print = 0xc350 + i1
while i1 < 0xFFFFFFFF:
    if i1 % iter_print == 0:
        #every n'th iteration, print progress and speed
        now = time.time()
        print("%.2f" % (((float(i1)+0.000001)/0xFFFFFFFF)*0x64))+"% - ",("%.2f" % (now - program_starts)) , "ms"
        program_starts = time.time()
    for i in xrange(0x2e,0x0,-0x1):
        a = hex(((cipher[i-1] + i1) % 0x100000000)^cipher[i])[0x2:0xa]
        # This will reject most keys that produce forbidden characters, but not all
        if a in deny: 
            break
        flag = 0x1
        text[i-0x1] = a 
    if flag == 0x1:
        if test in "".join(text):
            f = open('test.txt', 'a')
            f.write(str(i1)+"\n")
            f.close()
            print "Possible Keys are: "+str(i1)
    flag << 0x4
    i1+=4
print answer
