Mass=input("Enter the mass of the object in kg: ")
velocity=input("Enter the velocity of the object in m/s: ")
try:
    Mass=float(Mass)
    velocity=float(velocity)
    kinetic_energy=0.5*Mass*velocity**2
    print("The kinetic energy of the object is: ", kinetic_energy, "Joules")
except ValueError:
    print("Please enter valid numbers for mass and velocity.")