"""
Challenge 'Lotsa Dots'
15 seconds are given to analyze the picture
Circle`s centre is at 8x8 and every cell is +16 px apart
"""
from PIL import Image
import binascii


im = Image.open("stars.png")

#convert, otherwise ill get a stream of raw pixel data
rgb_im = im.convert('RGB')

#get height and width
a = im.getbbox()
width = a[2]
height = a[3]


binary = ""
i = 8
counter = 1

print "--------START--------\n"
while i < (height-1):    
    j=8
    temp = ""   
    while j<width-7:
        #as seen below this returns 3 variables for RGB
        r,g,b = rgb_im.getpixel((j,i))

        #returns 44 for orange and 233 for white-ish
        if(b == 44):            
            temp = temp+"0"
        else:
            temp = temp+"1"               
        j+=16        
    print '%s %2s %0s %s' % ("Row:",counter,"Byte:",temp)
    binary = binary+temp
    i+=16
    counter+=1
print "\n",binary
n = int(binary, 2)
print "\nAnswer:",
print "\n",binascii.unhexlify('%x' % n),"\n"
print "---------END---------\n"
