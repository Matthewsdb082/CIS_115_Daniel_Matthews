e = 0
c = 2.99 * 10**8
def calculate_energy(m):
    e=m*c**2
    return e

m = int(input("input a mass"))
e = calculate_energy(m)
print(f"the energy produced is {e:.2f} joules")
