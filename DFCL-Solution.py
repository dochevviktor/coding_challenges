import binascii
from array import array


# i did the bytes by hand,figured if hex dont
# work, bytes might since its repeated in the forums a lot

txt = (0xe5534ada,0xc53023aa,0xad55518a,0xc42671f8,0xa1471d94,0xd8676ce1,0xb11309c1,
             0xc27a64b1,0xae1f4a91,0xc73f2bfc,0xe74c5e8e,0x826c27e1,0xf74c4f80,0x81296ff3,
             0xee451996,0x8a6570e2,0xaa0709c2,0xc4687eec,0xe44a1589,0x903e79ec,0xe75117ce,
             0xc73864ee,0xbe57119c,0x9e367fef,0xe9530dc1)

mylist = []
answer = ""

#remove xor backwards, ripped off from the image decoder
for  i in range(len(txt)-1,0,-1):
    mylist.append(txt[i] ^ txt[i-1] )

#reverse mylist, idk why, prob becayse of backward thing
for  i in reversed(mylist):
 answer+= binascii.unhexlify('%x' % i)

print answer
