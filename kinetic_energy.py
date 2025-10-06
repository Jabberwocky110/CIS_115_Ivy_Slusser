#This code calculates kinetic energy.
mass = float(input("Enter the mass as a numerical value"))
#Each unit is assigned to a variable.
unit1 = ("kg")
print(f'The mass is {mass}{unit1}.')
velocity = float(input("Enter the velocity as a numerical value"))
unit2 = ("m/s")
print(f'The velocity is {velocity}{unit2}.')
#This function calculates and returns kinetic energy
def kinetic_energy(mass, velocity):
    kinetic_energy = ((mass * (velocity ** 2))/2)
    return kinetic_energy
calculation = kinetic_energy(mass, velocity)
unit3 = ("joules")
print(f'The kinetic energy is {calculation}{unit3}.')