# 4. check whether a triangle is valid using sides.

a = int(input('enter the first angle:'))
b = int(input('enter the secont angle:'))
c = int(input('enter the third angle:'))

if( a + b > c and b + c > a and a + c > b):
    print('triangle is valid')
else:
    print('triangle is invalid')