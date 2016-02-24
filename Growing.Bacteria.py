"""
Scientists have noted that a member of a strange bacteria species has a cycle of life like this:
Day 1: the bacterium is born from a division of his 'mother'.
Day 2: the bacterium divides itself into two bacteria (one of them is a brand new bacterium).
Day 3: the bacterium divides itself into two bacteria again (one of them is a brand new bacterium).
Day 4: the bacterium has already divided itself twice. Now it's ready to die.
Day 5: the bacterium dies.

A unique member of this kind has been collected by scientists. After 8 days, the population is 47.
The question is: after how many days will the entire population of bacteria originated by this
unique member reach the count of 1,000,000,000,000?
"""
start = 1
divide1 = 0
divide2 = 0
end = 0

day = 1;
total = 0
while(total<1000000000000): 
    end = divide2
    divide2 = divide1 
    divide1 = start
    start += divide2      
    total = (start + divide1 + divide2 + end)
    day+=1
print "Day: ",day


