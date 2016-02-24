cipher = ( 0x5499fa99, 0x1ee7d8da, 0x5df0b78b, 0x1cb0c18c, 0x10f09fc5, 0x4bb7fdae, 0x7fcb95ac,
           0xe494fbae, 0x8f5d90a3, 0xc766fdd7, 0xb7399ecc, 0xbf4af592, 0xf35c9dc2, 0x272be2a4,
           0x5e788697, 0x520febd8, 0x468c808c, 0x2e550ac9, 0x2b4d28b7, 0x4c166789, 0x33df0bec,
           0x67a96778, 0x0ffa0ce3, 0x44cd2a9a, 0x2dc208dc, 0x35c26a9d, 0x658b0fd7, 0x0d006482,
           0x46c90cf8, 0x28d72a79, 0x4ea94be5, 0x1bbc6995, 0x478505d3, 0x7b1a6b8d, 0xaf7408db,
           0xef7d7f9f, 0x76471cc6, 0xef1076b4, 0x6c911aa7, 0xe75a7ed3, 0x89630c8d, 0xf32b7fcb,
           0x697c1e89, 0x091c30be, 0x736a4cbf, 0xe27339bb, 0x9a2a52a2)


x = 334036501
k = 0

text = [""]*46
token = [""]*9
answer = ""

for i in range(46,0,-1):    
    k = (cipher[i-1] + x) % 0x100000000
    text[i-1] = k ^ cipher[i];
   

for i in range(0,46):
    token = hex(text[i]).rstrip("L").lstrip("0x") or "0"
    token = list(token)
    for j in range(0,8,2):
        l = chr(int(token[j]+token[j+1], 16))
        answer += l
print answer
