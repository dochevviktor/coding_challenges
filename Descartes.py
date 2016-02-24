import Tkinter as tk

"""
pasted the hex code from descartes into the bin translator and got the decimal values
(descartes invented the coordinate system, lets give it a shot)
writing answer in case I lose the lib somehow
"The answer is coordinate"
"""

a = [1, 6, 3, 6, 2, 4, 2, 6, 9, 3, 8, 3, 8, 1, 8,
     3, 9, 1, 8, 1, 16, 4, 15, 6, 19, 6, 18, 4, 19,
     1, 19, 3, 6, 2, 6, 2, 27, 3, 28, 3, 6, 6, 7, 6,
     10, 3, 11, 3, 14, 6, 14, 4, 23, 3, 22, 3, 2, 3,
     2, 1, 12, 1, 12, 3, 18, 2, 17, 3, 24, 6, 22, 6,
     5, 4, 5, 6, 15, 2, 16, 1, 24, 3, 26, 3, 17, 3,
     17, 1, 13, 1, 13, 3, 12, 6, 12, 4, 4, 3, 3, 3,
     6, 1, 6, 1, 4, 4, 4, 6, 3, 3, 3, 2, 14, 3, 16,
     3, 6, 4, 7, 4, 20, 4, 20, 6, 20, 1, 20, 3, 6,
     6, 6, 4, 4, 5, 5, 5, 6, 5, 7, 5, 11, 1, 10, 1,
     14, 3, 14, 1, 16, 2, 14, 2, 18, 2, 17, 1, 25,
     1, 25, 3, 3, 1, 4, 1, 4, 2, 3, 2, 4, 1, 4, 2,
     23, 3, 23, 1, 27, 1, 27, 3, 22, 3, 22, 1, 17,
     5, 16, 4, 17, 5, 18, 4, 13, 6, 14, 4, 13, 4, 13,
     6, 11, 3, 11, 1, 27, 1, 28, 1, 21, 1, 21, 3, 10,
     3, 10, 1, 12, 3, 13, 3, 12, 1, 13, 1, 22, 2, 23,
     2, 22, 6, 22, 4, 12, 6, 11, 6, 23, 5, 24, 4, 11,
     5, 12, 5, 22, 5, 24, 5, 11, 4, 11, 6, 24, 5, 24,
     6, 21, 6, 20, 6, 21, 1, 20, 3, 21, 5, 20, 5, 20,
     4, 21, 4, 27, 2, 28, 2, 16, 2, 16, 3]


import Tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Drawing lines to a canvas")
a = list(reversed(a))
cv = tk.Canvas(root,height="600",width="300",bg="white")
cv.pack()


for i in range(0,len(a)-3,4):    
    cv.create_line(a[i]*18,a[i+1]*18,a[i+2]*18,a[i+3]*18, width=4,fill="blue")

root.mainloop()
