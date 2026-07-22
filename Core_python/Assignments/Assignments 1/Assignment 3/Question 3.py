#3. check whether an triangle is valid using angles. 

a = int(input('enter thr first angle'))
b = int(input('enter the second angle'))
c = int(input('enter the third angle'))

if (a > 0 and b > 0 and c > 0 and a+b+c == 180):
    print('triangle is valid')
else:
    print('triangle is invalid')