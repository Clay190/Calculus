#Clay Kynor
#11.19.18

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

func = input("Input your function: ")
num = int(input("Input how many rectangles you want "))
a = float(input("Input the start of your range "))
b = float(input("input the end of your range "))

n = (b-a)/num
Ltotal = 0
Mtotal = 0
Rtotal = 0
SimpTotal = 0
y1 = 0
y2 = 0
y3 = 0

for i in range(0,num):
    x=(i*n)+a
    Ltotal += eval(func)*n
    y1 = eval(func)
    x = ((i*n)+a) + (n/2)
    Mtotal += eval(func)*n
    y2 = eval(func)
    x=((i+1)*n)+a
    Rtotal += eval(func)*n
    y3 = eval(func)
    SimpTotal += (y1+(4*y2)+y3)*(n/6)


TrapTotal = (Ltotal+Rtotal)/2

print("LRAM", Ltotal)
print("MRAM", Mtotal)
print("RRAM", Rtotal)
print("Trapezoid Area", TrapTotal)
print("Simpson's Area", SimpTotal)