#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = int(input('enter the marks of subject1:'))
m2 = int(input('enter the marks of subject2:'))
m3 = int(input('enter the marks of subject3:'))
m4 = int(input('enter the marks of subject4:'))
m5 = int(input('enter the marks of subject5:'))

per = (m1+m2+m3+m4+m5)/5

print('percentage=', per)

if(per >= 77):
    print('Grade:Distinction')
elif(per >= 65):
        print('Grade:First class')
elif(per >= 55):
            print('Grade:Second class')
elif(per >= 35):
                print('Grade:pass class')

    





