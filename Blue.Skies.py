from PIL import Image

"""
Image obviously lacked red color
Hex editor didnt show jack except a lot of 00s everywhere
After extracting red pixel data only, there were random 2s and 3s scattered
Folloing that, every 250th value was followed by a new line
Result was the answer spelled in kinda ASCII art and barely readable
After a quick fix, this thing makes a PNG using relevant pixel coordinates
"""

width = 0
height = 0

im = Image.open("blueskies.png")
im2 = Image.new("RGB", im.size, "white")

#print im.format, im.size, im.mode

source = im.getdata(0)# 0 = get me Red only
putpixel = im2.putpixel # init pixel writer

for i in source:    
    if i != 0:
        putpixel((width,height), (0,0,0)) # 0,0,0 in RGB = Black
    if width==250: # 250 is the blueskies.png width
        width = 0
        height +=1
    width+=1
im2.save("answer.png","PNG")
