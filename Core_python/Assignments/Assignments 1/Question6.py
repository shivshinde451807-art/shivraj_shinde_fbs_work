#WAP to input two angle from user and find third of the triangle
angle1 = int(input("Enter the first angle of triangle :"))
angle2 = int(input("Enter the second angle of triangle :"))
angle3 = 180 - (angle1 + angle2)
print("Third angle of triangle is :", angle3)