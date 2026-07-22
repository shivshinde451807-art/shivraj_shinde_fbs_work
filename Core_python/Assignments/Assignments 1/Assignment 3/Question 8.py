#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same.
#  If user enters the same number then show him success message otherwise failed. (Something like captcha) 

import random
userid = input('enter the userid:')
password = input('enter the password:')

if( userid == 'shivv' and password == 'shiv123'):
    captcha = random.randint(1000, 8888)
    print(f'your captcha = {captcha}')
    chuser = int(input('enter the captcha=>'))
    if (chuser == captcha):
        print('user login successfully..')
    else:
        print('invalid captcha..')
else:
            print('user is invalid..')
