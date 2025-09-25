#This code determines engergy in the Joules unit.
import math
#Each value and unit is assigned a variable.
mass = int(3) 
unit1 = ("kg")
Speed_of_Light = float(2.99 * (10 ** 8))
unit2 = ("m/s")
unit3 = ("kJ")
energy2 = int(mass * (Speed_of_Light ** 2))
def calculate_energy():
    m = float(input("Enter the mass of an object in kilograms."))
    energy = int(m * (Speed_of_Light ** 2))
    print(f'The energy calculated from the mass value you entered is {energy} {unit3}.')
calculate_energy()
print(f'The energy produced from a 3 kg object is {energy2} {unit3}')
