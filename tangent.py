#This code calculates the tangent for a triangle.
import math
def Theta():
    x = int(input("Enter the first side measure"))
    y = int(input("Enter the second side measure"))
    Angle = (math.atan2(y,x))
    #The angle is converted to degrees.
    Angle_in_Degrees = (180/math.pi) * Angle
    print(f'The angle theta is {Angle_in_Degrees: .2f} degrees.')
Theta()