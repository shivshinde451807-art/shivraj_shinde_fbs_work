#12. Check if given number is Armstrong Number

n = int(input('Enter a number: '))
original = n
count = 0
temp = n

while temp > 0:
    count = count + 1
    temp = temp // 10

sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == original:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
