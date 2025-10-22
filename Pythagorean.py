#This code determines the hypoteneuse of a right triangle
import math
def Hypotheneuse_calculator():
   x = int(input("Enter the first side measure"))
   y = int(input("Enter the second side measure"))
   c = math.sqrt((x * x) + (y * y))
   print(f'The hypotheneuse measures {c: .2f}.')
Hypotheneuse_calculator()