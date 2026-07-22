#5>. check whether triangle is equilateral, isosceles or scalene. 

a = int(input('enter first side:'))
b = int(input('enter the second side:'))
c = int(input('enter the third side:'))
if(a==b==c):
    print('euilateral triangle')
elif(a==b or b==c or a==c):
    print('isosceles triangle')
else:
    print('scalene triangle')