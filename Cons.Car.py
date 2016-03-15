import math
"""
 The idea here is to : 
 1) take the number, get its binary length that is close to a power of 2
    ex. if 'a' in binary is 11111 nearest pow of 2 is 8
    take this bin len and use it as a pow of 2
 2) take the doubled 'a' and subtract with 1)'s value output

"""
a = 123456789
print int((a*2)-(2**(math.ceil(math.log(a)/math.log(2)))))


"""
This is the Lisp/Schema that needed to be simplified and converted

(define (f n) 
 (do ((d (do ((i (- n 1) (- i 1)) # crazy for loops in loops
              (d '() (cons i d)))
             ((< i 0) d)) # bitshift ahoy!
         (append (cddr d) (list (car d)))))
     ((null? (cdr d)) (car d))))
(display (f 123456789))
"""


  
