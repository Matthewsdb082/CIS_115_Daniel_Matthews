import math
x= int( input("input x value for triangle"))
y= int (input("input y value fot triangle"))
pie =3.145


def angle (x,y):
 T = math.atan2(y,x)
 Out = T * 180 / pie
 return Out

Out = angle(x,y)
print(f"the angle is {Out:.2f} deg")