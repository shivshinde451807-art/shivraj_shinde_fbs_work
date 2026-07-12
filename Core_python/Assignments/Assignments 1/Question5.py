#WAP to enter P, T, R and calculate compound Intrest.
P = float(input("Enter principal amount: "))
T = float(input("Enter Time in years: "))
R = float(input("Enter Rate of Interest: "))
CI = P + (1 + R/100) ** T- P
print ("compound Interest is:", CI)