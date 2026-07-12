#Program to find Roots of Quadratic Equation.
import cmath
x = float(input("Enter coefficient x :"))
y = float(input("enter the coefficient y :"))
z = float(input("Enter the coefficient z :"))

#discriminant calculation
dis = (y**2) - (4*x*z)


#find two roots
root1 = (-y - cmath.sqrt(dis)) / (2*x)
root2 = (-y + cmath.sqrt(dis)) / (2*x)
print("The roots are {0} and {1} ".format(root1, root2))

