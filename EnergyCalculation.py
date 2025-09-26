#This code determines engergy in the Joules unit.
#Each value and unit for the 3 kg object is assigned a variable.
mass = int(3) 
unit1 = ("kg")
Speed_of_Light = float(2.99 * (10 ** 8))
unit2 = ("m/s")
unit3 = ("J")
energy2 = int(mass * (Speed_of_Light ** 2))
#This function converts both of the energies to scientific notation.
def scientific_notation(number):
   scientific_notation = (f'{number: .2e}')
   #The scientific notation has to be returned so that it can be printed later in the code.
   return scientific_notation
def calculate_energy():
    #The user can enter the mass of an object as a float.
    m = float(input("Enter the mass of your object: The mass should be entered as a numerical value."))
    #The user entered mass is entered as a numerical value before a unit is added.
    print(f'The mass of your object is {m} {unit1}')
    energy = int(m * (Speed_of_Light ** 2))
    #The scientific notation function is called within the print, and the user created energy is printed in scientific notation.
    print(f'The energy calculated from the mass value you entered is {scientific_notation(energy)} {unit3}.')
    #The calculate energy function is called.
calculate_energy()
#The assigned mass in printed in scientific notation.
print(f'The energy produced from a 3 kg object is {scientific_notation(energy2)} {unit3}.')
