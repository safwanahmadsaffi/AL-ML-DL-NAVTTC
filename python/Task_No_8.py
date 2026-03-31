#Finding area of the triangle by user input

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the thitd side: "))

#Semi Parameter
s = (a + b + c) / 2

area = ( s * (s-a) * (s-b) * (s-c) ) ** 0.5

print(f"Area of the triangle is = {area}")