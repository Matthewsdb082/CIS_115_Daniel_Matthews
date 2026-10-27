def max(N1,N2):
    if N1>N2:
     return N1
    else:
     return N2

N1 = int(input("input int number 1 "))
N2 = int(input("input int number 2 "))
larger=max(N1,N2)

if larger ==N1:
 print(f"N1 is larger", N1)
else:
     print(f"N2 is larger", N2)