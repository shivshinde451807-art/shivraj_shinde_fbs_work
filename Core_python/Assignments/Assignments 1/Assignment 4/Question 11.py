#11. Check if given number is Strong Number

n = int(input('Enter a number: '))
original = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == original:
    print('Strong Number')
else:
    print('Not a Strong Number')