import numpy
x = int(input('Pick a Number: '))
if  len(x) == 1:
    print('This is a good number')
elif len(x) == 2:
    if x%2 == 0:
        print('This is the best number')
    else:
        print('This is better number')    
else:
    print('Horrible Number')

y = int(input('Pick a second number')) 
if y%2 != 0:
    if y%3 == 0:
        print('Odd and divisible by 3')
    else:
        print('Odd')
elif y%2 == 0:
    if y%3 == 0:
        print('Even and divisible by 3')
    else:
        print('Even')





        
         




