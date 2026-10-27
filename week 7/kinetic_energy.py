def kinetic_energy(mass,velocity):
    Ke= .5*mass*velocity**2
    return Ke

mass = float(input("input the mass in KG: "))
velocity= float(input("input the velocity meter per sec: "))

Ke = kinetic_energy(mass,velocity)

print(f"the kenetic enerhy is {Ke} joules")