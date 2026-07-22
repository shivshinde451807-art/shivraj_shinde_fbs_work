#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 

gender = (input('enter the gender(m/f):'))
age = int(input('enter the age:'))
if(gender == 'f'):
    if(age >=   18):
        print('Girl are eligible for marriage.')
    else:
        print('Girl are not eligible for marriage.') 
else:
    if(age>=21):
        print('boy are eligible for marriage.')   
    else:
            print('boy are not eligible for marriage.')